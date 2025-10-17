"""
Command-line interface for RhythmFace.

Provides CLI commands for running the application and diagnostics.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence

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
    # TODO: Implement application main loop
    # 1. Initialize audio listener
    # 2. Initialize lip-sync engine
    # 3. Initialize renderer
    # 4. Run main event loop
    # 5. Cleanup on exit
    print("RhythmFace application starting...")
    print(f"FPS: {config.lipsync.fps}")
    print(f"Window: {config.graphics.window_width}x{config.graphics.window_height}")
    print("TODO: Implement main application loop")
    return 0


def run_diagnostics(config: RhythmFaceConfig) -> int:
    """
    Run diagnostic tests for audio devices and rendering.

    Args:
        config: Application configuration

    Returns:
        Exit code (0 = success)
    """
    # TODO: Implement diagnostics
    # 1. List available audio input devices
    # 2. Test audio capture with RMS display
    # 3. Test rendering with FPS counter
    # 4. Test asset loading
    print("RhythmFace Diagnostics")
    print("=" * 40)
    print("\nTODO: Implement diagnostics")
    print("- Audio device enumeration")
    print("- Microphone test")
    print("- Rendering test")
    print("- Asset verification")
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
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
    run_parser = subparsers.add_parser(
        "run",
        help="Start the RhythmFace application",
    )

    # Diagnose command
    diagnose_parser = subparsers.add_parser(
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

