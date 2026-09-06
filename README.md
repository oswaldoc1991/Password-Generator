# Passwor-Generator
This project will focus on producing and generate passwords based on the users request by using python code

# Password Generator

A simple Python CLI application that generates secure random passwords and checks their strength.

## Features

* Generate secure random passwords
* Choose password length
* Include or exclude lowercase letters, uppercase letters, numbers, and symbols
* Generate multiple passwords
* Check password strength
* Allow or exclude ambiguous characters

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Password-Generator/password_generator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Run the program

Linux:

```bash
PYTHONPATH=src python -m passgen.cli --length 18 --strength
```

Windows PowerShell:

```powershell
$env:PYTHONPATH="src"
python -m passgen.cli --length 18 --strength
```

## Examples

Generate a password:

```bash
PYTHONPATH=src python -m passgen.cli
```

Generate an 18-character password and check its strength:

```bash
PYTHONPATH=src python -m passgen.cli --length 18 --strength
```

Generate 5 passwords:

```bash
PYTHONPATH=src python -m passgen.cli --length 18 --count 5
```

View all available options:

```bash
PYTHONPATH=src python -m passgen.cli --help
```

## Built With

* Python
* `argparse`
* `secrets`
* `dataclasses`

## Author

Oswaldo Cabrera
