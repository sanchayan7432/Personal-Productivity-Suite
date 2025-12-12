# Personal-Productivity-Suite
Building a comprehensive productivity suite with multiple integrated tools (calculator, notes manager, timer, file organizer) using object-oriented design, file handling, and user-friendly interfaces

Project Overview
The Personal Productivity Suite is a multi-tool Python application designed to help users manage daily tasks efficiently.
 This project was built as part of the Developers’ Arena Python Developer Internship (Month 1 – Task 1).
The suite includes:
🧮 Calculator


📝 Notes Manager (JSON Storage)


⏱ Timer


📂 File Organizer


🔁 Backup Manager


🔢 Unit Converter


🌐 Streamlit GUI Interface


The application follows modular architecture, object-oriented programming, and persistent data storage using JSON, text files, and CSV.
Objectives
Build a real-world Python project using OOP, file handling, JSON persistence, and clean architecture.


Provide both CLI and GUI (Streamlit) interfaces.


Demonstrate modularity, error handling, and Python best practices.


Prepare a fully deployable GitHub-ready codebase.


Specifications
✔ Calculator
Safe mathematical expression evaluation


Prevents malicious expressions using ast


Works with +, –, *, /, %, parentheses, power, etc.


✔ Notes Manager
Create, edit, delete, search notes


JSON-based persistent storage


Export notes to .txt


✔ Timer
Countdown timer


Stopwatch functionality


Logs history


✔ File Organizer
Automatically organizes files into categories:
Images


Videos


Documents


Audio


Archives


Others
✔ Backup Manager
Creates timestamped project backups


Restores backups


✔ Unit Converter
Length (km ↔ m ↔ cm)


Weight (kg ↔ g ↔ mg)


Temperature (C ↔ F ↔ K)


✔ Streamlit GUI (gui.py)
Sidebar menu for tool selection


Fully working web UI


Easy to use for non-technical users
Installation and Setup
### Option 1 — Install using virtual environment (Recommended)
cd productivity-suite
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate # Mac/Linux

Install required packages:
pip install -r requirements.txt
### Option 2 — Run without venv
Simply install dependencies globally:
pip install -r requirements.txt
How To Run The Project
👉 Run CLI version
python main.py


👉 Run GUI (Streamlit) version
streamlit run gui.py
