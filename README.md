# Password Generator

A simple Python CLI application that generates secure random passwords and checks their strength.

## Features

* Generate secure random passwords
* Choose password length
* Include or exclude lowercase and uppercase letters
* Include or exclude numbers and symbols
* Generate multiple passwords
* Check password strength
* Allow or exclude ambiguous characters

## Requirements

Before running the project, make sure you have:

* Python 3.10 or newer
* Git
* A terminal such as PowerShell, Terminal, or Bash

---

# Installation

## 1. Clone the Repository

First, clone the project from GitHub:

```bash
git clone https://github.com/oswaldoc1991/Password-Generator.git
```

Enter the project folder:

```bash
cd Password-Generator/password_generator
```

---

# Windows Setup

## 1. Create a Virtual Environment

Open PowerShell inside the project folder and run:

```powershell
python -m venv .venv-windows
```

## 2. Activate the Virtual Environment

```powershell
.\.venv-windows\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(.venv-windows)
```

## 3. Set the Python Source Path

```powershell
$env:PYTHONPATH="src"
```

## 4. Run the Program

```powershell
python -m passgen.cli --length 18 --strength
```

---

# Linux Setup

## 1. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Depending on your Linux installation, `python` may also work:

```bash
python -m venv .venv
```

## 2. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

After activation, the terminal should show:

```text
(.venv)
```

## 3. Run the Program

```bash
PYTHONPATH=src python -m passgen.cli --length 18 --strength
```

If your system uses `python3` instead:

```bash
PYTHONPATH=src python3 -m passgen.cli --length 18 --strength
```

---

# macOS Setup

## 1. Create a Virtual Environment

```bash
python3 -m venv .venv
```

## 2. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

## 3. Run the Program

```bash
PYTHONPATH=src python3 -m passgen.cli --length 18 --strength
```

---

# Using the Password Generator

Once your environment is activated, you can customize how passwords are generated.

## Generate an 18-Character Password

```bash
python -m passgen.cli --length 18
```

On Linux/macOS, include the source path if necessary:

```bash
PYTHONPATH=src python -m passgen.cli --length 18
```

## Generate a Password and Check Its Strength

```bash
python -m passgen.cli --length 18 --strength
```

## Generate Multiple Passwords

For example, generate five passwords:

```bash
python -m passgen.cli --length 18 --count 5
```

## Generate a Password Without Symbols

```bash
python -m passgen.cli --length 18 --no-symbols
```

## Generate a Password Without Numbers

```bash
python -m passgen.cli --length 18 --no-digits
```

## Generate a Password Without Uppercase Letters

```bash
python -m passgen.cli --length 18 --no-upper
```

## Generate a Password Without Lowercase Letters

```bash
python -m passgen.cli --length 18 --no-lower
```

## Allow Ambiguous Characters

```bash
python -m passgen.cli --length 18 --allow-ambiguous
```

## View All Available Commands

```bash
python -m passgen.cli --help
```

---

# Starting the Program Again Later

You only need to **create the virtual environment once**.

### Windows

When returning to the project:

```powershell
cd Password-Generator\password_generator

.\.venv-windows\Scripts\Activate.ps1

$env:PYTHONPATH="src"

python -m passgen.cli --length 18 --strength
```

### Linux

```bash
cd Password-Generator/password_generator

source .venv/bin/activate

PYTHONPATH=src python -m passgen.cli --length 18 --strength
```

### macOS

```bash
cd Password-Generator/password_generator

source .venv/bin/activate

PYTHONPATH=src python3 -m passgen.cli --length 18 --strength
```

---

# Command Options

| Option              | Description                                       |
| ------------------- | ------------------------------------------------- |
| `-l`, `--length`    | Choose the password length                        |
| `--no-lower`        | Disable lowercase letters                         |
| `--no-upper`        | Disable uppercase letters                         |
| `--no-digits`       | Disable numbers                                   |
| `--no-symbols`      | Disable symbols                                   |
| `--allow-ambiguous` | Allow ambiguous characters such as O, 0, l, and 1 |
| `--count`           | Generate multiple passwords                       |
| `--strength`        | Check the generated password's strength           |
| `-h`, `--help`      | Show all available commands                       |

---

# Built With

* Python
* `argparse`
* `secrets`
* `dataclasses`
* Regular Expressions (`re`)

## Author

Oswaldo Cabrera
