# Primora Programming Language

[![Python application](https://github.com/Jothankato05/primora-playground/actions/workflows/python-app.yml/badge.svg)](https://github.com/Jothankato05/primora-playground/actions/workflows/python-app.yml)
[![Lint with Pylint](https://github.com/Jothankato05/primora-playground/actions/workflows/pylint.yml/badge.svg)](https://github.com/Jothankato05/primora-playground/actions/workflows/pylint.yml)
[![Deploy Docs](https://github.com/Jothankato05/primora-playground/actions/workflows/deploy-docs.yml/badge.svg)](https://github.com/Jothankato05/primora-playground/actions/workflows/deploy-docs.yml)
[![Publish Python Package](https://github.com/Jothankato05/primora-playground/actions/workflows/publish-python-package.yml/badge.svg)](https://github.com/Jothankato05/primora-playground/actions/workflows/publish-python-package.yml)
[![codecov](https://codecov.io/gh/Jothankato05/primora-playground/branch/main/graph/badge.svg?token=976e6a56-cf3a-44db-a435-47eb07c149bd)](https://codecov.io/gh/Jothankato05/primora-playground)
[![CodeQL](https://github.com/Jothankato05/primora-playground/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Jothankato05/primora-playground/actions/workflows/codeql-analysis.yml)

<div align="center">
  <h2>🚀 Code as Command. Syntax as Strategy. Execution as Power.</h2>
  <p><strong>An AI-native programming language for predictive and manipulative programming</strong></p>
  
  [🎮 Try Online](https://primora-playground.netlify.app) | [📖 Documentation](https://primora-docs.windsurf.build) | [💬 Community](#community) | [🎯 Roadmap](#roadmap)
</div>

---

## ✨ What is Primora?

**Primora** is a revolutionary, security-first programming language designed for the next generation of developers. It seamlessly integrates:

- 🤖 **AI-Native Constructs** - Built-in AI operations for prediction, manipulation, and analysis
- 🛡️ **Security-First Design** - Automatic source sanitization and code review
- 🧠 **Psychological Scripting** - Behavioral influence and persuasion mechanics
- 🔄 **Python Transpilation** - Easy integration with existing Python ecosystems
- 💡 **Natural Language Interface** - Write code in plain English
- 🎯 **Domain-Specific Extensions** - Perfect for ethical hacking, AI development, and strategic systems

## 🎯 Key Features

### AI-Powered Programming
```primora
predict threat of network_traffic using ai.model("intrusion_detector")
if threat.is("malicious") {
    manipulate attacker using tactic("decoy", tone="aggressive")
    echo "Threat neutralized" using frame("confident")
}
```

### Natural Language Interface
```primora
# Describe what you want in plain English
search "latest AI breakthroughs" as results
summarize results as summary
echo summary
```

### Universal Commands
```primora
# Built-in utilities for common tasks
weather London
wiki "Albert Einstein"
currency 100 USD to EUR
news "artificial intelligence"
```

### Real-Time Collaboration
```primora
# Share your code instantly with a URL
# Multiple developers can edit simultaneously
# Built-in Firebase integration
```

## 🚀 Quick Start

### Installation

#### Via pip (Recommended)
```bash
pip install primora-lang
```

#### From Source
```bash
git clone https://github.com/Jothankato05/Primora-Playground.git
cd Primora-Playground
pip install -r requirements.txt
```

### Usage

#### Interactive REPL
```bash
primora
```

#### Run a File
```bash
primora script.pri
```

#### Transpile to Python
```bash
primora-transpile input.pri -o output.py
```

#### Start the Backend Server
```bash
primora-backend
```

#### Language Server (LSP)
```bash
primora-lsp
```

## 📚 Examples

### 1. Threat Detection System
```primora
listen source("http://network.scan") as traffic
predict threat of traffic using ai.model("intrusion_detector")

if threat.is("malicious") {
    manipulate attacker using tactic("decoy", tone="aggressive")
    echo "🛡️ Threat neutralized" using frame("confident")
} else {
    echo "✅ Network secure" using frame("calm")
}
```

### 2. Data Analysis Pipeline
```primora
fetch url("https://api.example.com/data") as dataset
summarize dataset as insights
plot insights as "Data Visualization"
email to "team@company.com" subject "Analysis Complete" body insights
```

### 3. Behavioral Influence
```primora
manipulate user_response using tactic("urgency", tone="persuasive")
if user_response.is("positive") {
    echo "Action completed successfully!"
}
```

## 🏗️ Architecture

Primora consists of several core components:

- **Lexer** (`primora_parser.py`) - Tokenizes Primora code
- **Parser** (`primora_parser.py`) - Builds Abstract Syntax Trees
- **Interpreter** (`primora_interpreter.py`) - Executes Primora programs
- **Transpiler** (`primora_transpiler.py`) - Converts to Python
- **Standard Library** (`primora_stdlib.py`) - Built-in functions and modules
- **LSP Server** (`primora_lsp.py`) - IDE integration
- **Backend API** (`primora_backend.py`) - Web service for playground
- **Natural Language** (`primora_nl.py`) - NL to code conversion

## 🎮 Interactive Playground

Visit our [online playground](https://primora-playground.netlify.app) to:
- ✍️ Write and run Primora code instantly
- 🤝 Collaborate in real-time with others
- 🤖 Get AI-powered code suggestions
- 📖 Access built-in documentation
- 🔗 Share your programs with unique URLs

## 🛠️ Use Cases

### Security Research
- Intrusion detection systems
- Automated penetration testing
- Threat response automation
- Security analysis pipelines

### AI Development
- Behavioral prediction models
- Sentiment analysis systems
- Recommendation engines
- Natural language processing

### Strategic Systems
- Psychological operations
- Persuasion automation
- Influence campaigns
- Decision support systems

### Data Science
- Automated data pipelines
- Visualization systems
- Report generation
- API integration

## 🌍 Community

Join our growing community:

- **Discord** - Real-time chat and support
- **Twitter** - Follow [@PrimoraLang](https://twitter.com/PrimoraLang) for updates
- **GitHub Discussions** - Ask questions and share ideas
- **YouTube** - Tutorial videos and live coding sessions

## 🗺️ Roadmap

### v0.1.0 (Current)
- ✅ Core language implementation
- ✅ Interactive REPL
- ✅ Web playground
- ✅ Basic AI integration
- ✅ Python transpilation

### v0.2.0 (Next)
- 🔄 Enhanced standard library
- 🔄 VS Code extension
- 🔄 Improved error messages
- 🔄 Debugging capabilities
- 🔄 Package manager

### v1.0.0 (Future)
- 📅 Self-hosted compilation
- 📅 JIT compiler
- 📅 Advanced AI models
- 📅 Plugin system
- 📅 Enterprise features

## 💖 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

See our [Contributing Guide](CONTRIBUTING.md) for more details.

### Development Setup
```bash
# Clone the repository
git clone https://github.com/Jothankato05/Primora-Playground.git
cd Primora-Playground

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run linter
pylint primora_*.py
```

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Python Software Foundation
- Flask and Flask-CORS teams
- HuggingFace for AI model APIs
- The open-source community

## 🔗 Links

- **Website**: [primora-lang.org](https://primora-playground.netlify.app)
- **Documentation**: [primora-docs.windsurf.build](https://primora-docs.windsurf.build)
- **GitHub**: [Jothankato05/Primora-Playground](https://github.com/Jothankato05/Primora-Playground)
- **PyPI**: [primora-lang](https://pypi.org/project/primora-lang/) (coming soon)

---

<div align="center">
  <p><strong>Built with ❤️ by the Primora Team</strong></p>
  <p>Code as Command. Syntax as Strategy. Execution as Power.</p>
</div>
