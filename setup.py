from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="prompt-engineering-playground",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A toolkit for exploring and analyzing prompt engineering techniques",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/prompt-engineering-playground",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.20.0",
        "anthropic>=0.7.0",
        "openai>=0.27.0",
        "python-dotenv>=0.21.0",
        "pandas>=1.5.3",
        "numpy>=1.24.2",
    ],
    extras_require={
        "dev": [
            "pytest>=7.2.2",
            "pytest-cov>=4.0.0",
            "black>=23.3.0",
            "flake8>=6.0.0",
            "mypy>=1.2.0",
        ],
        "viz": [
            "plotly>=5.14.1",
            "matplotlib>=3.7.1",
        ],
    },
    entry_points={
        "console_scripts": [
            "prompt-playground=src.streamlit_app:main",
        ],
    },
)