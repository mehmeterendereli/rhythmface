# Contributing to RhythmFace

Thank you for your interest in contributing to RhythmFace! This document provides guidelines and instructions for contributing to the project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Guidelines](#testing-guidelines)
- [Pull Request Process](#pull-request-process)
- [Issue Reporting](#issue-reporting)

## 🤝 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

Examples of behavior that contributes to a positive environment:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Unacceptable Behavior

- Trolling, insulting/derogatory comments, and personal attacks
- Public or private harassment
- Publishing others' private information without permission
- Other conduct which could reasonably be considered inappropriate

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Poetry for dependency management
- Git
- A GitHub account

### Setup Development Environment

1. **Fork the repository** on GitHub

2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/rhythmface.git
   cd rhythmface
   ```

3. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/yourusername/rhythmface.git
   ```

4. **Install dependencies**:
   ```bash
   poetry install --with dev
   ```

5. **Install pre-commit hooks**:
   ```bash
   poetry run pre-commit install
   ```

6. **Generate assets**:
   ```bash
   poetry run python -m rhythmface.assets.generator
   ```

7. **Run tests to verify setup**:
   ```bash
   poetry run pytest
   ```

## 🔄 Development Workflow

### Branch Strategy

- `main`: Stable production code
- `develop`: Integration branch for features
- `feature/*`: Feature branches
- `bugfix/*`: Bug fix branches
- `hotfix/*`: Critical production fixes

### Working on a Feature

1. **Create a feature branch**:
   ```bash
   git checkout develop
   git pull upstream develop
   git checkout -b feature/my-awesome-feature
   ```

2. **Make your changes** following [coding standards](#coding-standards)

3. **Write/update tests** for your changes

4. **Run the full test suite**:
   ```bash
   poetry run pytest --cov=rhythmface
   ```

5. **Run linters and formatters**:
   ```bash
   poetry run black rhythmface tests
   poetry run isort rhythmface tests
   poetry run ruff check rhythmface tests
   poetry run mypy --strict rhythmface
   ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: Add awesome feature"
   ```

   Use [conventional commits](https://www.conventionalcommits.org/):
   - `feat:` New feature
   - `fix:` Bug fix
   - `docs:` Documentation changes
   - `style:` Code style changes (formatting, etc.)
   - `refactor:` Code refactoring
   - `test:` Adding or updating tests
   - `chore:` Maintenance tasks

7. **Push to your fork**:
   ```bash
   git push origin feature/my-awesome-feature
   ```

8. **Open a Pull Request** on GitHub

## 📏 Coding Standards

### Python Style Guide

We follow PEP 8 with some modifications enforced by our tools:

- **Line length**: 100 characters (Black default)
- **Type hints**: Required for all functions (mypy strict mode)
- **Docstrings**: Required for all public modules, classes, and functions
- **Import order**: Handled by isort

### Type Hints

All functions must have type hints:

```python
def process_audio(data: np.ndarray, sample_rate: int) -> AudioFeatures:
    """
    Process audio data and extract features.

    Args:
        data: Audio samples as numpy array
        sample_rate: Sample rate in Hz

    Returns:
        Extracted audio features
    """
    pass
```

### Docstring Format

We use Google-style docstrings:

```python
def my_function(arg1: str, arg2: int) -> bool:
    """
    One-line summary of function.

    More detailed description if needed. Can span
    multiple lines.

    Args:
        arg1: Description of arg1
        arg2: Description of arg2

    Returns:
        Description of return value

    Raises:
        ValueError: When invalid input is provided
    """
    pass
```

### Code Organization

- **Module-level imports**: At the top, grouped by standard library, third-party, local
- **Constants**: UPPER_CASE at module level
- **Classes**: PascalCase
- **Functions/variables**: snake_case
- **Private members**: Leading underscore (_private_method)

### Design Principles

- **Interface Segregation**: Prefer small, focused interfaces
- **Dependency Injection**: Pass dependencies explicitly
- **Strategy Pattern**: For pluggable algorithms
- **Type Safety**: Leverage mypy strict mode
- **Testability**: Write code that's easy to test

## 🧪 Testing Guidelines

### Test Structure

```python
# tests/test_module.py
import pytest

from rhythmface.module import MyClass


class TestMyClass:
    """Test suite for MyClass."""

    def test_initialization(self) -> None:
        """Test that MyClass initializes correctly."""
        obj = MyClass()
        assert obj is not None

    def test_method_with_valid_input(self) -> None:
        """Test method behavior with valid input."""
        obj = MyClass()
        result = obj.method(valid_input)
        assert result == expected_output

    def test_method_with_invalid_input(self) -> None:
        """Test method raises exception with invalid input."""
        obj = MyClass()
        with pytest.raises(ValueError):
            obj.method(invalid_input)
```

### Test Coverage

- **Target**: 80%+ code coverage
- **Focus**: Critical paths, error handling, edge cases
- **Tools**: pytest, pytest-cov

```bash
# Run with coverage
poetry run pytest --cov=rhythmface --cov-report=html

# View coverage report
open htmlcov/index.html
```

### Test Types

1. **Unit Tests**: Test individual components in isolation
2. **Integration Tests**: Test component interactions
3. **Smoke Tests**: Verify basic functionality
4. **Fixture Tests**: Use pytest fixtures for complex setup

## 🔍 Pull Request Process

### Before Submitting

- [ ] All tests pass (`poetry run pytest`)
- [ ] Code is formatted (`poetry run black .`)
- [ ] Imports are sorted (`poetry run isort .`)
- [ ] No linting errors (`poetry run ruff check .`)
- [ ] Type checking passes (`poetry run mypy --strict rhythmface`)
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated (if applicable)

### PR Template

When opening a PR, include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
Describe testing done

## Checklist
- [ ] Tests pass
- [ ] Code formatted
- [ ] Documentation updated
- [ ] Type hints added
```

### Review Process

1. Automated checks run (CI pipeline)
2. Code review by maintainers
3. Address feedback
4. Final approval
5. Merge to develop

### PR Guidelines

- **Keep PRs focused**: One feature/fix per PR
- **Write clear descriptions**: Explain what and why
- **Reference issues**: Link to related issues
- **Update documentation**: Keep docs in sync
- **Be responsive**: Address review comments promptly

## 🐛 Issue Reporting

### Bug Reports

Use the bug report template and include:

- **Description**: Clear description of the bug
- **Steps to Reproduce**: Minimal steps to reproduce
- **Expected Behavior**: What should happen
- **Actual Behavior**: What actually happens
- **Environment**: OS, Python version, package versions
- **Logs/Screenshots**: Error messages, screenshots if applicable

### Feature Requests

Use the feature request template and include:

- **Use Case**: What problem does this solve?
- **Proposed Solution**: Your idea for implementation
- **Alternatives**: Other solutions you've considered
- **Additional Context**: Any other relevant information

### Issue Labels

- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Documentation improvements
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed
- `question`: Further information requested

## 📝 Documentation

### Update Documentation

When adding features or changing APIs:

1. **Update docstrings** in code
2. **Update README.md** if needed
3. **Update Sphinx docs** in `docs/`
4. **Add examples** for new features

### Building Docs Locally

```bash
cd docs
poetry run make html
open _build/html/index.html
```

## 🎯 Areas for Contribution

We especially welcome contributions in:

- **New lip-sync strategies**: ML-based, formant analysis, etc.
- **Performance improvements**: Optimization, profiling
- **Audio features**: Additional feature extraction methods
- **Graphics**: Enhanced rendering, animations
- **Documentation**: Tutorials, examples, translations
- **Tests**: Increase coverage, add edge cases
- **CI/CD**: Workflow improvements
- **Packaging**: Distribution improvements

## 💡 Getting Help

- **Documentation**: Check [docs](https://rhythmface.readthedocs.io)
- **Discussions**: Use [GitHub Discussions](https://github.com/yourusername/rhythmface/discussions)
- **Issues**: Search existing issues first
- **Discord**: Join our community server (if applicable)

## 🏆 Recognition

Contributors are recognized in:

- GitHub contributors list
- CONTRIBUTORS.md file
- Release notes

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to RhythmFace! 🎉**

