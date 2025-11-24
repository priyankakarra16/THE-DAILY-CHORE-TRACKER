#Project Statement: The Daily Chore Tracker
#1. Problem Statement
The goal is to create a minimalist, dependency-free CLI utility for tracking small, immediate tasks. This addresses the need for a simple organizational tool that works directly within the development environment, avoiding the complexity of external apps.

#2. Scope of the Project
#In Scope
Task Management: Adding, viewing, and marking tasks as complete.
Data Structure: Using a list of dictionaries for in-memory storage.
Interface: All interaction is via a menu-based console (CLI).
#Out of Scope
Persistence: The list is not saved between sessions.
External Dependencies: Uses only built-in Python features.
Advanced Features: No deletion, editing, or external database integration.

#3. Target Users
Beginning Programmers/Students: For learning fundamental Python concepts (functions, loops, lists).
Developers/System Administrators: For managing quick, temporary tasks in the terminal.

#4. High-Level Features
Feature Category: DescriptionTask
Creation: Inputs and adds new tasks to the list.
Status Tracking: Uses a boolean status (done: True/False) for tracking completion.
User Interaction: Simple, numbered menu system for action selection.
Error Checking: Validates user input to prevent crashes from invalid numbers or input types.
