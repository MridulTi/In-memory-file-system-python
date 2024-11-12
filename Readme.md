# CLI File Operations Tool

A simple Command Line Interface (CLI) application written in Python that mimics basic file operations like `mkdir`, `cd`, `ls`, `cat`, `touch`, `echo`, `mv`, `cp`, and `rm`. This tool allows users to perform these file operations directly from the terminal. It’s a modular CLI app where each command is implemented in its own separate file for easy maintenance and extension.

## Features

- **mkdir**: Create a new directory.
- **cd**: Change the current directory, including support for navigating to the parent directory using `..`, the root directory using `/`, and any specified absolute path.
- **ls**: List the contents of the current directory or a specified directory.
- **cat**: Display the contents of a file.
- **touch**: Create a new empty file.
- **echo**: Write text to a file.
- **mv**: Move a file or directory to another location.
- **cp**: Copy a file or directory to another location.
- **rm**: Remove a file or directory.

## Installation

### Prerequisites

Make sure you have Python 3.x installed on your system. You can check the version of Python installed by running:

```bash
python --version
```

If you don’t have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

### Clone the Repository

First, fork and clone the repository to your local system using Git:

```bash
git clone https://github.com/yourusername/cli-file-operations.git
```

### Install Dependencies

Navigate to the project directory:

```bash
cd cli-file-operations
```

This project does not have any external dependencies, as it only uses Python's built-in libraries (`os`, `shutil`, etc.), so no installation of extra packages is necessary. However, it’s always a good practice to work in a virtual environment:

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### Running the CLI Tool

Once the repository is cloned and dependencies are set up, you can run the application by executing:

```bash
python cli_app/main.py
```

This will start a command-line interface where you can use the following commands:

---

## Available Commands

### **mkdir**: Create a new directory
- **Usage**: `mkdir <directory_path>`
- **Description**: Creates a new directory at the specified path.
- **Example**:
  - `mkdir new_folder` — Creates a directory named `new_folder` in the current working directory.
  - `mkdir /home/user/projects` — Creates a directory at the specified absolute path.

### **cd**: Change the current directory
- **Usage**: `cd <directory_path>`
- **Description**: Changes the current working directory. Supports navigation to the parent directory using `..`, to the root directory using `/`, and to a specified absolute or relative path.
- **Example**:
  - `cd ..` — Moves up one level to the parent directory.
  - `cd /home/user/projects` — Navigates to the absolute path `/home/user/projects`.
  - `cd ~` — This will take you to the root directory (`/`).

### **ls**: List the contents of the current directory
- **Usage**: `ls <directory_path>`
- **Description**: Lists the contents (files and directories) of the current directory or a specified directory.
- **Example**:
  - `ls` — Lists the contents of the current directory.
  - `ls /home/user/projects` — Lists the contents of the directory `/home/user/projects`.

### **cat**: Display the contents of a file
- **Usage**: `cat <file_path>`
- **Description**: Displays the contents of the specified file in the terminal.
- **Example**:
  - `cat file.txt` — Displays the contents of `file.txt` in the terminal.
  - `cat /home/user/documents/notes.txt` — Displays the contents of the file at the specified path.

### **touch**: Create a new empty file
- **Usage**: `touch <file_path>`
- **Description**: Creates a new empty file at the specified location. If the file already exists, it updates the file’s timestamp.
- **Example**:
  - `touch newfile.txt` — Creates an empty file named `newfile.txt` in the current directory.
  - `touch /home/user/documents/file.txt` — Creates an empty file at the specified absolute path.

### **echo**: Write text to a file
- **Usage**: `echo '<text>' > <file_path>`
- **Description**: Writes the provided text to a file. If the file does not exist, it will be created. The `>` operator overwrites the file, while `>>` appends the text.
- **Example**:
  - `echo 'Hello, World!' > hello.txt` — Creates a file `hello.txt` and writes 'Hello, World!' into it.
  - `echo 'Appending text' >> file.txt` — Appends the text to `file.txt`.

### **mv**: Move a file or directory to another location
- **Usage**: `mv <source_path> <destination_path>`
- **Description**: Moves a file or directory from the source path to the destination path.
- **Example**:
  - `mv file.txt /home/user/new_folder/` — Moves `file.txt` to `/home/user/new_folder/`.
  - `mv old_file.txt new_file.txt` — Renames `old_file.txt` to `new_file.txt`.

### **cp**: Copy a file or directory to another location
- **Usage**: `cp <source_path> <destination_path>`
- **Description**: Copies a file or directory from the source path to the destination path.
- **Example**:
  - `cp file.txt /home/user/backup/` — Copies `file.txt` to `/home/user/backup/`.
  - `cp -r folder/ /home/user/backup/` — Copies the directory `folder/` and all its contents to the backup location.

### **rm**: Remove a file or directory
- **Usage**: `rm <file_or_directory_path>`
- **Description**: Removes the specified file or directory. Use the `-r` flag to remove directories and their contents recursively.
- **Example**:
  - `rm file.txt` — Removes `file.txt` from the current directory.
  - `rm -r folder/` — Removes the directory `folder/` and its contents.

---

## Exiting the CLI

To exit the CLI interface, you can use the `exit` command:

```bash
exit
```

## Code Structure

The project is organized into the following files:

- **`main.py`**: The main entry point for the CLI tool. Handles user input and calls the appropriate command functions.
- **`commands/`**: This directory contains separate Python files for each command (`mkdir.py`, `cd.py`, `ls.py`, `cat.py`, `touch.py`, `echo.py`, `mv.py`, `cp.py`, `rm.py`). Each file defines the functionality for a specific command.
- **`utils/`**: This directory can be used for shared utility functions, though this project does not require any currently.
- **`__init__.py`**: Required to mark directories as Python packages, allowing easy imports across files.

---
Thank you for using this CLI File Operations Tool. Happy coding! 🚀
