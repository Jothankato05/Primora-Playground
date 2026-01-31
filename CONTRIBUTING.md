# Contributing to Primora

**Thank you for your interest in contributing to Primora!**

We love your input! We want to make contributing to Primora as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## Getting Started

### 1. Fork the Repository
Click the "Fork" button at the top right of the repository page.

### 2. Clone Your Fork
```bash
git clone https://github.com/YOUR_USERNAME/Primora-Playground.git
cd Primora-Playground
```

### 3. Set Up Development Environment
```bash
# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pylint pytest pytest-cov

# Verify installation
python primora_interpreter.py
```

### 4. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

## Development Workflow

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=.

# Run specific test file
pytest test_backend.py
```

### Code Quality
```bash
# Run linter
pylint primora_*.py

# Format code (if using black)
black primora_*.py
```

### Testing the Backend
```bash
# Start the backend server
python primora_backend.py

# In another terminal, test endpoints
curl http://localhost:5001/self_reflect
```

### Testing the Frontend
```bash
# Serve the website locally
cd website
python -m http.server 8000

# Open http://localhost:8000 in your browser
```

## Making Changes

### Good Pull Request Guidelines

1. **Keep it focused** - One feature or fix per PR
2. **Write clear commit messages** - Use present tense ("Add feature" not "Added feature")
3. **Update documentation** - If you change functionality, update the docs
4. **Add tests** - New features should include tests
5. **Follow the code style** - Match the existing code style

### Commit Message Format
```
type(scope): Short description

Longer description if needed

Fixes #issue_number
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```bash
feat(parser): Add support for async operations
fix(interpreter): Handle edge case in variable assignment
docs(readme): Update installation instructions
```

## Reporting Bugs

### Before Submitting a Bug Report
- Check the [issue tracker](https://github.com/Jothankato05/Primora-Playground/issues) for existing reports
- Try to reproduce the issue with the latest version
- Collect relevant information (OS, Python version, error messages)

### How to Submit a Bug Report
Use the issue template and include:

1. **Description** - Clear description of the bug
2. **Steps to Reproduce** - Exact steps to trigger the bug
3. **Expected Behavior** - What should happen
4. **Actual Behavior** - What actually happens
5. **Environment** - OS, Python version, Primora version
6. **Code Sample** - Minimal code that reproduces the issue
7. **Screenshots** - If applicable

## Suggesting Features

We love new ideas! Before suggesting a feature:

1. **Check existing issues** - Someone may have already suggested it
2. **Consider the scope** - Does it fit Primora's mission?
3. **Provide use cases** - Explain why this would be useful

### Feature Request Template
```markdown
## Feature Description
Clear description of the proposed feature

## Use Cases
Real-world scenarios where this would be useful

## Proposed Implementation
(Optional) How you think it could be implemented

## Alternatives Considered
Other approaches you've thought about
```

## Areas to Contribute

### High Priority
- Bug fixes
- Documentation improvements
- Standard library functions
- Test coverage
- Internationalization

### Medium Priority
- UI/UX improvements
- Performance optimizations
- Developer tools
- Package management

### Advanced
- Compiler optimizations
- AI model integration
- IDE extensions
- JIT compilation

## Documentation

Documentation is just as important as code! We need help with:

- **Tutorials** - Step-by-step guides for beginners
- **How-To Guides** - Solutions to common problems
- **Reference** - API documentation
- **Examples** - Real-world use cases
- **Videos** - Video tutorials and demos

## Recognition

Contributors will be:
- Listed in the CONTRIBUTORS.md file
- Mentioned in release notes
- Featured on the website (for significant contributions)

## Pull Request Process

1. **Update documentation** - Reflect any changes in the relevant docs
2. **Update tests** - Ensure all tests pass
3. **Run linter** - Make sure code passes pylint checks
4. **Update CHANGELOG** - Add entry for your changes
5. **Request review** - Tag maintainers for review
6. **Address feedback** - Make requested changes promptly
7. **Merge** - A maintainer will merge once approved

### Pull Request Checklist
- [ ] Code follows the project style
- [ ] Self-review of code completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
- [ ] Tests added/updated
- [ ] All tests pass
- [ ] No linting errors
- [ ] CHANGELOG updated

## Security

Found a security vulnerability? **Do NOT open a public issue.**

Instead, email security@primora-lang.org (or create a private security advisory on GitHub).

## Getting Help

Need help contributing?

- **Discord** - Join our community server
- **Discussions** - Ask on GitHub Discussions
- **Email** - Reach out to the maintainers

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for making Primora better!
