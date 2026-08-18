# Personal Journal Manager

A simple command-line Personal Journal Manager built with Python.

This project allows users to create, view, search, and delete journal entries while automatically storing the date and time of each entry.

## Features

* Add a new journal entry
* View all saved journal entries
* Search entries using a keyword or date
* Delete all journal entries
* Automatically records the date and time
* Stores entries in a `journal.txt` file
* Handles common file-related errors
* Handles permission errors
* Uses Object-Oriented Programming

## Technologies Used

* Python 3
* `os` module
* `datetime` module
* File Handling
* Exception Handling
* Object-Oriented Programming

## Project Structure

```text
FILE-OPERATOR/
│
├── journal.py
├── journal.txt
├── README.md
└── assets/
    └── journal-manager-output.png
```

The `journal.txt` file is created automatically when the first journal entry is added.

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
```

### 2. Open the Project Folder

```bash
cd your-repository-name
```

### 3. Run the Program

```bash
python journal.py
```

## Main Menu

```text
===================================
Welcome to Personal Journal Manager!
===================================

Please select an option:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

Enter your choice:
```

## Add a New Entry

Select option `1` to add a new journal entry.

Example:

```text
Enter your choice: 1

Enter your journal entry:
Today was a productive day.
I completed my Python project and learned a lot.

Entry added successfully!
```

The entry is saved with the current date and time.

Example:

```text
[2026-08-18 11:30:25]
Today was a productive day.
I completed my Python project and learned a lot.
```

## View All Entries

Select option `2` to display all saved journal entries.

```text
Your Journal Entries:
------------------------------
[2026-08-18 11:30:25]
Today was a productive day.
I completed my Python project and learned a lot.
```

## Search for an Entry

Select option `3` and enter a keyword or date.

Example:

```text
Enter your choice: 3

Enter a keyword or date to search: Python

Matching Entries:
------------------------------
[2026-08-18 11:30:25]
Today was a productive day.
I completed my Python project and learned a lot.
```

The search is case-insensitive.

## Delete All Entries

Select option `4` to delete all journal entries.

The program asks for confirmation:

```text
Enter your choice: 4

Are you sure you want to delete all entries? (yes/no): yes

All journal entries have been deleted.
```

If `no` is entered, the deletion is cancelled.

## Exit

Select option `5` to close the program.

```text
Thank you for using Personal Journal Manager. Goodbye!
```

## Output

Add your screenshot inside the `assets` folder and use the following Markdown:

```markdown
## Output

![Personal Journal Manager Output](assets/journal-manager-output.png)
```

## Concepts Demonstrated

### Object-Oriented Programming

The project uses a `JournalManager` class to organize the application.

```python
class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"
```

### File Handling

The project uses different file modes:

```python
"r"
"a"
"w"
"x"
```

These modes are used for reading, appending, writing, and creating files.

### Exception Handling

The program handles different errors using `try` and `except`.

```python
try:
    ...
except FileNotFoundError:
    ...
except PermissionError:
    ...
except Exception as e:
    ...
```

### Date and Time

Each journal entry automatically receives a timestamp.

```python
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

## Future Improvements

Possible improvements for this project include:

* Edit an existing journal entry
* Delete a specific journal entry
* Filter entries by date
* Add entry numbering
* Create a graphical interface using Tkinter
* Add password protection
* Export journal entries to PDF
* Store data using JSON or SQLite
