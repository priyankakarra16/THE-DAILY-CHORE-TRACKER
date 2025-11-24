# THE-DAILY-CHORE-TRACKER
The Daily Chore Tracker is a friendly, menu-driven command-line tool written in Python. It's a fundamental project focused on making complex code simple and readable, allowing users to track their pending and completed chores efficiently.
#Project Titile-The Daily Chore Tracker

#Overview of the Project
A simple, menu-driven Command-Line Interface (CLI) application built in Python 3. Its purpose is to demonstrate proficiency in fundamental Python concepts—specifically using lists of dictionaries to manage data and implementing core program logic via functions and a while loop interface.

#Features
Add Tasks: Quickly add descriptive new chores.
View Tasks: Display all items with their index number and status ([ PENDING ] or [ COMPLETE ]).
Mark as Done: Update a selected task's status from pending to complete.
User-Friendly Code: The code is intentionally verbose and heavily commented for maximum readablity.

#Technologies/Tools Used
Language: Python 3.x
Data Structure: List of Dictionaries
Environment: Command-Line Interface (CLI)
Version Control: Git & GitHub

#Steps to Install & Run the Project
Prerequisite: Ensure Python 3 is installed.
Clone:
Bash
git clone [Your Repository URL Here]
cd your-repo-name
Run: Execute the main script:
Bash
python human_todo_list.py

#Instructions for Testing
Test 1 (Add & View): Use menu option 1 (Add) three times, then use option 2 (View) to confirm all three tasks are listed as [ PENDING ].
Test 2 (Mark Done): Use option 3 (Mark as finished) and input a valid number (e.g., 2). Then use option 2 to confirm the status of that task is now [ COMPLETE ].
Test 3 (Error Check): Attempt to mark an invalid task number (e.g., 99) or non-number text; the program must display a clear error message and return to the main menu without crashing.
Test 4 (Exit): Use option 4 to successfully terminate the program.
