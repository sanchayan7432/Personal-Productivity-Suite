# Personal Productivity Suite

Build a comprehensive productivity suite with multiple integrated tools (calculator, notes manager, timer, file organizer) using object-oriented design, file handling, and user-friendly interfaces

📘 Project Overview

The Personal Productivity Suite is a complete, modular, and extensible Python application designed to improve daily productivity.
It bundles multiple essential utilities into one structured system:
```
A safe mathematical calculator

A feature-rich notes manager with JSON persistence

A timer and stopwatch tool

A file organizer for automatic folder cleanup

A unit converter

A backup system to store project snapshots

A Streamlit-based GUI
```
This project demonstrates strong skills in:
```
✔ Python Programming
✔ Modular Code Architecture
✔ Object-Oriented Programming
✔ JSON, TXT, ZIP file handling
✔ CLI & GUI application development
✔ Error handling & validation
✔ Unit testing with Python
```

🌟 Features
🧮 1. Calculator
```
Uses Python’s AST for safe parsing

Prevents arbitrary code execution

Supports arithmetic operations, parentheses, power, modulo, etc.
```
📝 2. Notes Manager
```
Create, read, edit, delete, search notes

JSON-based persistent storage

Export notes to .txt

Auto timestamps every note
```
📂 3. File Organizer

Automatic sorting of files based on type:
```
Type	      Examples
Images	      png, jpg, gif
Videos	      mp4, mov, avi
Documents	  pdf, docx, txt
Audio	      mp3, wav
Archives	  zip, rar
Others	      all else
```
⏱ 4. Timer & Stopwatch
```
Countdown timer

Stopwatch with lap tracking

Logs saved to text file
```
🔢 5. Unit Converter

Convert between:
```
Length (km/m/cm/mm)

Weight (kg/g/mg)

Temperature (°C/°F/K)
```
🗂 6. Backup Manager
```
Creates project-wide .zip backup

Restores from an existing backup
```
🖥 7. Streamlit GUI
```
Beautiful GUI interface

Sidebar navigation

Simplified usage for non-technical users
```

🛠 Tech Stack
```
Python 3.10+

Streamlit – For GUI

JSON / TXT / ZIP – Persistent storage

AST module – Secure calculator

OS / shutil / zipfile – File operations

Unit testing with unittest
```

🧱 Project Architecture
```
productivity-suite/
│
├── main.py                # Main CLI entry point
├── gui.py                 # Streamlit GUI interface
├── requirements.txt       # Required Python libraries
├── README.md              # Documentation
│
├── modules/
│   ├── __init__.py
│   ├── calculator.py
│   ├── notes_manager.py
│   ├── file_organizer.py
│   ├── timer.py
│   ├── unit_converter.py
│   ├── backup.py
│   ├── utils.py
│   └── data/
│       └── notes.json
│
├── tests/
│   ├── test_calculator.py
│   └── test_notes.py
│
└── examples/
    └── sample.txt
```

⚙ Installation & Setup
1. Clone the Repository
```
git clone https://github.com/your-username/productivity-suite.git
cd productivity-suite
```
2. Create a Virtual Environment
Windows:
```
python -m venv venv
venv\Scripts\activate
```
Linux / Mac:
```
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```

▶ How to Run
Run the CLI
```
python main.py
```

Run the GUI (Streamlit)
```
streamlit run gui.py
```

📘 Detailed Module Documentation
🧮 calculator.py
Provides:
```
Safe expression parsing

Secure AST-based evaluator

Blocks prohibited expressions like "__import__('os').system('rm -rf /')"
```
Function:
```
evaluate_expr(expression: str) -> float
```
📝 notes_manager.py
Features:
```
Add note

Edit note

Delete note

Search note

Export notes to .txt

Persistent JSON storage
```
JSON Structure:
```
[
  {
    "id": 1,
    "title": "Shopping List",
    "content": "Milk\nEggs\nBread",
    "created": "2025-01-01 10:30",
    "modified": "2025-01-01 10:30"
  }
]
```
📂 file_organizer.py

Automatically organizes files into sub-folders based on extensions.

Example usage:
```
organize_directory("C:/Users/Downloads/")
```
⏱ timer.py
```
Stopwatch

Countdown timer

Lap tracking

Logs stored in /modules/data/timer_log.txt
```
🔢 unit_converter.py

Supports 3 categories:
```
Length:

km ↔ m ↔ cm ↔ mm

Weight:

kg ↔ g ↔ mg

Temperature:

Celsius ↔ Fahrenheit ↔ Kelvin
```
🗂 backup.py
Creates .zip backup:
```
create_backup(source_path, backup_directory)
```
Restore backup:
```
restore_backup(zip_path, extract_to)
```
🔧 utils.py

Utility helpers:
```
Safe input

Timestamp generator

Valid path checker
```
🌐 Graphical User Interface

The project includes a full Streamlit GUI, located in gui.py.

Features:
```
Sidebar tool selection

Real-time calculator

Editable notes interface

Drag & drop file organizer

Timer with live updates

Interactive unit converter
```
Run:
```
streamlit run gui.py
```

🧪 Testing (Unit Tests)

Test files are included in /tests/.

Run all tests:
```
python -m unittest discover tests
```

🛠 Troubleshooting Guide
❌ ModuleNotFoundError: No module named 'modules'

Run from project root:
```
python -m tests.test_calculator
```
❌ Streamlit not installed

Install:
```
pip install streamlit
```
❌ notes.json corrupted

Delete it:
```
modules/data/notes.json
```

It auto-recreates.

❌ GUI not launching

Run:
```
streamlit run gui.py
```

👤 Author
```
Sanchayan Ghosh | sanchayan7432@gmail.com
Python Developer | LLM Researcher and Prompt Engineering Security Researcher | Former Research Intern, MIST Lab, IIT Bhilai
```


