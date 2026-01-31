from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="primora-lang",
    version="0.1.0",
    author="Jothankato05",
    author_email="",
    description="An AI-native programming language for predictive and manipulative programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jothankato05/Primora-Playground",
    project_urls={
        "Bug Tracker": "https://github.com/Jothankato05/Primora-Playground/issues",
        "Documentation": "https://primora-docs.windsurf.build",
        "Source Code": "https://github.com/Jothankato05/Primora-Playground",
        "Playground": "https://primora-playground.netlify.app",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Interpreters",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=find_packages(),
    py_modules=[
        "primora_parser",
        "primora_interpreter",
        "primora_transpiler",
        "primora_stdlib",
        "primora_lsp",
        "primora_nl",
        "primora_backend"
    ],
    python_requires=">=3.8",
    install_requires=[
        "flask>=2.0.0",
        "flask-cors>=3.0.0",
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "pylint>=2.0",
        ],
        "viz": [
            "matplotlib>=3.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "primora=primora_interpreter:main",
            "primora-transpile=primora_transpiler:main",
            "primora-lsp=primora_lsp:main",
            "primora-backend=primora_backend:main",
        ],
    },
    keywords="programming-language ai interpreter compiler dsl primora",
)
