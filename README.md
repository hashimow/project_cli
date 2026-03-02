# Python Project Management CLI Tool

## Overview
This is a simple interactive **Command-Line Interface (CLI) project management tool** built in Python.  
It allows you to **manage users, projects, and tasks** through a menu-driven interface.  
All data is saved locally in `data.json` so it persists between runs.

## Features
- Add, edit, remove, and list users
- Add, edit and list projects
- Add, edit, complete, and list tasks
- Interactive menu-based CLI
- Data persistence using JSON

## Setup Instructions

1. Clone the repository (or download the ZIP)

git clone https://github.com/
<hashimow>/project_cli.git
cd project_cli


2. Install dependencies:

pip install -r requirements.txt


3. Run the project:

python3 main.py


## How to Use

1. Run `python3 main.py`  
2. Follow the menu:
   - Type a number (1–12) to choose an action
   - Enter required information when prompted
   - Exit saves all changes automatically

## File Structure


project_cli/
├─ main.py # Interactive CLI menu
├─ models.py # User, Project, Task classes
├─ utils.py # JSON helpers (load/save)
├─ data.json # Local storage
├─ requirements.txt
└─ README.md


## Notes

- Data persists in `data.json`.  
- Make sure to exit the program using menu option **12** to save data.
