"""
Command-line interface for RhythmFace.

Provides CLI commands for running the application and diagnostics.
"""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from rhythmface import __version__
from rhythmface.config import RhythmFaceConfig, get_default_config


def run_app(config: RhythmFaceConfig) -> int:
    """
    Run the main RhythmFace application.

    Args:
        config: Application configuration

    Returns:
        Exit code (0 = success)
    """
    from rhythmface.audio.mic_listener import MicListener
    from rhythmface.graphics.renderer import Renderer
    from rhythmface.logic.lipsync_engine import LipSyncEngine, MouthShape

    print("RhythmFace application starting...")
    print(f"FPS: {config.lipsync.fps}")
    print(f"Window: {config.graphics.window_width}x{config.graphics.window_height}")
    print("\nInitializing...")

    # Initialize audio listener
    mic_listener = MicListener(config.audio)

    # Initialize renderer
    renderer = Renderer(config.graphics)
    renderer.initialize()

    # Initialize lip-sync engine
    engine = LipSyncEngine(config.lipsync)

    print("✓ Audio listener initialized")
    print("✓ Renderer initialized")
    print("✓ Lip-sync engine initialized")
    print("\nStarting microphone capture...")

    # Start audio capture
    try:
        mic_listener.start()
        print("✓ Microphone active")
    except RuntimeError as e:
        print(f"✗ Failed to start microphone: {e}")
        print("Falling back to demo mode...")
        mic_listener = None  # type: ignore

    print("\nPress ESC or Q to quit, F for fullscreen")
    print("Speak into your microphone to animate the character!\n")

    # Main loop - real-time lip-sync
    running = True
    current_shape = MouthShape.CLOSED

    while running:
        # Handle events
        running = renderer.handle_events()

        # Get audio features and update lip-sync
        if mic_listener is not None and mic_listener.is_active():
            features = mic_listener.get_latest_features()
            if features is not None:
                engine.update(features)
                current_shape = engine.get_current_shape()

        # Render current shape
        renderer.render_frame(current_shape)

        # Update window title with FPS and status
        fps = renderer.get_fps()
        mode = "LIVE" if mic_listener and mic_listener.is_active() else "DEMO"
        renderer.set_window_title(
            f"RhythmFace [{mode}] - {current_shape.value} - FPS: {fps:.1f}"
        )

    # Cleanup
    if mic_listener is not None:
        mic_listener.stop()
    renderer.cleanup()
    print("\nRhythmFace closed. Goodbye!")
    return 0


def run_diagnostics(config: RhythmFaceConfig) -> int:  # noqa: C901
    """
    Run diagnostic tests for audio devices and rendering.

    Args:
        config: Application configuration

    Returns:
        Exit code (0 = success)
    """
    import time

    from rhythmface.audio.mic_listener import MicListener
    from rhythmface.graphics.renderer import Renderer

    print("RhythmFace Diagnostics")
    print("=" * 60)

    # 1. List available audio input devices
    print("\n[1/4] Audio Input Devices:")
    print("-" * 60)
    try:
        devices = MicListener.list_devices()
        if devices:
            for device in devices:
                print(f"  [{device['index']}] {device['name']}")
                print(f"      Channels: {device['channels']}, "
                      f"Sample Rate: {device['sample_rate']} Hz")
        else:
            print("  ✗ No audio input devices found!")
    except Exception as e:
        print(f"  ✗ Error listing devices: {e}")

    # 2. Test audio capture with RMS display
    print("\n[2/4] Microphone Test (5 seconds):")
    print("-" * 60)
    print("  Speak into your microphone...")
    mic_listener = MicListener(config.audio)
    try:
        mic_listener.start()
        print("  ✓ Microphone started")

        for _ in range(50):  # 5 seconds at ~10Hz
            time.sleep(0.1)
            features = mic_listener.get_latest_features()
            if features:
                bar_length = int(features.rms_energy * 50)
                bar = "█" * bar_length
                status = "SPEECH" if features.is_speech else "silence"
                print(f"\r  Energy: {bar:<50} [{status}]", end="", flush=True)

        print("\n  ✓ Microphone test complete")
        mic_listener.stop()
    except Exception as e:
        print(f"\n  ✗ Microphone test failed: {e}")

    # 3. Test rendering with FPS counter
    print("\n[3/4] Rendering Test (3 seconds):")
    print("-" * 60)
    from rhythmface.logic.lipsync_engine import MouthShape

    renderer = Renderer(config.graphics)
    try:
        renderer.initialize()
        print("  ✓ Renderer initialized")

        start_time = time.time()
        frame_count = 0
        shapes = [MouthShape.CLOSED, MouthShape.A, MouthShape.O, MouthShape.E]
        shape_idx = 0

        while time.time() - start_time < 3.0:
            if not renderer.handle_events():
                break

            shape_idx = (shape_idx + 1) % len(shapes)
            renderer.render_frame(shapes[shape_idx])
            frame_count += 1

        elapsed = time.time() - start_time
        avg_fps = frame_count / elapsed if elapsed > 0 else 0
        print(f"  ✓ Rendered {frame_count} frames in {elapsed:.2f}s ({avg_fps:.1f} FPS)")

        renderer.cleanup()
    except Exception as e:
        print(f"  ✗ Rendering test failed: {e}")

    # 4. Test asset loading
    print("\n[4/4] Asset Verification:")
    print("-" * 60)
    from pathlib import Path

    assets_dir = Path(__file__).parent / "assets"
    required_assets = ["base.png", "mouth_closed.png", "mouth_A.png",
                      "mouth_O.png", "mouth_E.png"]

    all_present = True
    for asset in required_assets:
        asset_path = assets_dir / asset
        if asset_path.exists():
            size = asset_path.stat().st_size
            print(f"  ✓ {asset} ({size:,} bytes)")
        else:
            print(f"  ✗ {asset} MISSING")
            all_present = False

    print("\n" + "=" * 60)
    if all_present:
        print("✓ All diagnostics passed!")
    else:
        print("✗ Some diagnostics failed - see above")
    print("=" * 60)

    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """
    Main entry point for CLI.

    Args:
        argv: Command-line arguments (defaults to sys.argv)

    Returns:
        Exit code
    """
    parser = argparse.ArgumentParser(
        prog="rhythmface",
        description="Real-time lip-sync animation for 2D characters",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    parser.add_argument(
        "--config",
        type=Path,
        help="Path to configuration YAML file",
        metavar="PATH",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Run command
    subparsers.add_parser(
        "run",
        help="Start the RhythmFace application",
    )

    # Diagnose command
    subparsers.add_parser(
        "diagnose",
        help="Run diagnostic tests",
    )

    args = parser.parse_args(argv)

    # Load configuration
    if args.config:
        try:
            config = RhythmFaceConfig.from_yaml(args.config)
        except FileNotFoundError:
            print(f"Error: Configuration file not found: {args.config}", file=sys.stderr)
            return 1
        except Exception as e:
            print(f"Error loading configuration: {e}", file=sys.stderr)
            return 1
    else:
        config = get_default_config()

    # Execute command
    if args.command == "run":
        return run_app(config)
    elif args.command == "diagnose":
        return run_diagnostics(config)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
