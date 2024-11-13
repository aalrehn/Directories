# 🍎 Virtual File System Simulator

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen.svg)](#)
[![Coverage Status](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)](#)

A Python application that simulates a virtual file system, allowing users to create, move, and delete directories through a command-line interface.

## 📖 Table of Contents

- [Description](#-description)
- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Testing](#-testing)
- [Requirements](#-requirements)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

## 📝 Description

This application provides a simple simulation of a hierarchical file system. Users can perform operations like creating directories, moving directories, deleting directories, and listing the current directory structure.

Example commands:

- `CREATE fruits`
- `MOVE fruits/apples vegetables`
- `DELETE fruits/apples`
- `LIST`

## ✨ Features

- **Create Directories**: Easily create directories and nested subdirectories.
- **Move Directories**: Move directories to different locations within the file system.
- **Delete Directories**: Remove directories and their contents.
- **List Structure**: Display the current directory structure in a hierarchical format.
- **Command Parsing**: Interpret and execute commands from an input file.
- **Unit Testing**: Comprehensive tests using `pytest` to ensure code reliability.



## 🚀 Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/aalrehn/Directories.git
   cd Directories

2. **Install Dependencies** 
```
pip3 install -r requirements.txt
```
**(Optional but recommended)**

```
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
## Run the application
   ```
   python3 directories.py
```


## 🧪 Testing

1. Run Unit Tests
From the project root directory, execute:
```
   pytest
```
## 📚 Usage

1. **Prepare the Input File**

Ensure input.txt is in the project root directory with the commands you wish to execute. Example content: ** 
```
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
DELETE fruits/apples
DELETE foods/fruits/apples
LIST

```





## View the Output

The output will be written to output.txt in the project root directory.

## Example Output:
```

CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
fruits
  apples
    fuji
grains
vegetables
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
foods
  fruits
    apples
      fuji
  grains
  vegetables
    squash
DELETE fruits/apples
Cannot delete fruits/apples - fruits does not exist
DELETE foods/fruits/apples
LIST
foods
  fruits
  grains
  vegetables
    squash

```



## 📁 Project Structure
```
├── Logger
│   ├── __pycache__
│   │   └── logger_module.cpython-312.pyc
│   └── logger_module.py
├── README.md
├── filesystem
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── command_executor.cpython-312.pyc
│   │   ├── command_interpreter.cpython-312.pyc
│   │   ├── directory_structure.cpython-312.pyc
│   │   └── file_input_reader.cpython-312.pyc
│   ├── command_executor.py
│   ├── command_interpreter.py
│   ├── directory_structure.py
│   └── file_input_reader.py
├── input.txt
├── main.py
├── output.txt
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-312.pyc
    │   ├── test_command_executor.cpython-312-pytest-8.3.3.pyc
    │   ├── test_command_interpreter.cpython-312-pytest-8.3.3.pyc
    │   ├── test_directory_structure.cpython-312-pytest-8.3.3.pyc
    │   ├── test_file_input_reader.cpython-312-pytest-8.3.3.pyc
    │   └── test_logger_module.cpython-312-pytest-8.3.3.pyc
    ├── test_command_executor.py
    ├── test_command_interpreter.py
    ├── test_directory_structure.py
    ├── test_file_input_reader.py
    └── test_logger_module.py
    ```