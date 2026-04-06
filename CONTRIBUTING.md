# Contributing to Pickleball Paddle Discord Bot

Thank you for your interest in contributing! Here's how you can help.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/paddle-discord-bot.git
   cd paddle-discord-bot
   ```
3. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   ```
4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Workflow

### Running Locally
```bash
# Set up your .env file (copy from .env.example)
cp .env.example .env
# Edit .env with your Discord token and channel ID

# Run the bot
python bot.py
```

### Testing Changes
- Test scraper changes independently:
  ```bash
  python scraper.py
  ```
- Test database changes:
  ```bash
  python database.py
  ```

## What to Contribute

### Bug Fixes
- Found a bug? Create an issue first describing the problem
- Fork, fix, and submit a pull request
- Include details on how you tested the fix

### Feature Ideas
- **New data sources**: Add scrapers for additional pickleball organizations
- **Improved notifications**: Enhanced Discord embeds, threading, etc.
- **Better error handling**: Catch edge cases in scrapers
- **Documentation**: Clarify setup, add examples, improve guides
- **Performance**: Optimize scraping speed or database queries

### Code Quality
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test your changes before submitting a PR
- Update documentation if your change affects user-facing features

## Pull Request Process

1. **Ensure your code works:**
   ```bash
   python bot.py  # Test locally
   ```
2. **Commit with clear messages:**
   ```bash
   git commit -m "feat: add support for [new feature]"
   # or
   git commit -m "fix: resolve [bug description]"
   ```
3. **Push to your fork:**
   ```bash
   git push origin feature/your-feature-name
   ```
4. **Open a Pull Request** with:
   - Clear description of changes
   - Why you made this change
   - Any breaking changes or dependencies added
   - Screenshots/logs if applicable

## Code Style

- **Python**: Follow [PEP 8](https://pep8.org/)
- **Comments**: Explain the *why*, not the *what*
- **Function names**: Use descriptive, lowercase names with underscores
- **Variables**: Clear names over clever abbreviations

### Example:
```python
# Good
def scrape_upaa():
    """Scrape UPA-A approved paddles from their official site."""
    # ...

# Avoid
def get_paddles():
    """Get paddles."""
    # ...
```

## Reporting Issues

Found a problem? Create an issue with:
- **Title**: Clear, concise description
- **Description**: What went wrong, expected vs. actual behavior
- **Steps to reproduce**: How to trigger the issue
- **Environment**: OS, Python version, relevant logs
- **Screenshots**: If applicable

## Questions?

- Open a Discussion on GitHub
- Check existing issues/PRs—your question might already be answered
- Be respectful and patient

## Recognition

Contributors will be acknowledged in:
- The main README.md
- GitHub's contributor graph
- Release notes (for significant contributions)

---

**Thank you for making this project better!** 🎉
