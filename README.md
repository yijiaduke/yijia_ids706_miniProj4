# yijia_ids706_miniProj4

## CI/CD Badge
[![CI](https://github.com/yijiaduke/yijia_ids706_miniProj4/actions/workflows/hello.yml/badge.svg)](https://github.com/yijiaduke/yijia_ids706_miniProj4/actions/workflows/hello.yml)

## Python Template

This project is a Python project skeleton that uses GitHub Actions with a matrix configuration to test across multiple Python versions.

## File Structure

- **`Makefile`**: Provides commands for setup, testing, linting, and formatting the project.
- **`.github/workflows/`**: Contains the CI/CD workflows for GitHub, which trigger actions like setup, linting, and testing when code is pushed to the repository across multiple Python versions.
- **`main.py`**: Contains simple Python functions for addition and subtraction.
- **`test_main.py`**: Contains test cases using pytest for the functions in main.py.

## Setup

### 1. Clone the Repository

```bash
git clone git@github.com:yijiaduke/yijia_ids706_miniProj4.git
```

### 2. Open the Repository in Visual Studio Code

- Reopen in the container using the .devcontainer configuration.
- Rebuild the container if necessary, ensuring Docker is running on your computer.

### 3. Install dependencies
Run the following command to install all required dependencies:

```bash
make install
```

## Usage
- make install: Installs dependencies specified in requirements.txt.
- make format: Formats Python files using Black.
- make lint: Lints Python files using Pylint, ignoring specific patterns.
- make test: Runs tests using pytest and generates a coverage report.
- make clean: Removes pytest cache.

## CI/CD Setup
- GitHub Actions Workflow
The project uses a matrix build setup in GitHub Actions to test the code across multiple Python versions (3.7, 3.8, 3.9, and 3.11). The workflow is located in the .github/workflows/ directory.


