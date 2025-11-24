
the_list_of_chores = []

# --- FUNCTION BLOCK ---

def add_a_new_chore(chore_description):
    """
    This function takes a description from the user and adds it 
    to our main chore list. It defaults the status to "Not Done".
    """
    new_chore_item = {
        "chore_description": chore_description,
        "status_is_done": False
    }
    
    # We append the new item to the end of the list.
    the_list_of_chores.append(new_chore_item)
    print(f"\n[CONFIRMATION] >>> Added the chore: '{chore_description}'")

def show_all_chores():
    """
    This function loops through the entire list and prints each item 
    in a clean, human-readable format, including its index and status.
    """
    # First, we check if the list is empty. No point in showing nothing!
    if not the_list_of_chores:
        print("\n[NOTE] --- The list is currently empty. Time to add a chore! ---")
        return  # Stop the function if the list is empty

    print("\n==================================")
    print("      CURRENT CHORE LIST")
    print("==================================")
    
    # We use a traditional counting loop for clarity.
    current_index = 0
    while current_index < len(the_list_of_chores):
        
        # Pull the specific chore item from the list
        current_chore = the_list_of_chores[current_index]
        
        # Determine the status text based on the boolean value
        if current_chore["status_is_done"]:
            status_text = "[ COMPLETE ]"
        else:
            status_text = "[ PENDING ]"
            
        # We present the number to the user (starting at 1, not 0)
        user_number = current_index + 1
        
        print(f"[{user_number}] {status_text} | {current_chore['chore_description']}")
        
        # Increment the counter for the next loop iteration
        current_index = current_index + 1
        
    print("==================================")

def mark_chore_as_finished(user_input_number):
    """
    This function changes the 'status_is_done' flag for a specific chore.
    It includes checks to ensure the user input is a valid list item.
    """
    
    # Convert the user's string input into a whole number
    try:
        chosen_number = int(user_input_number)
    except ValueError:
        print("\n[ERROR] !!! That was not a valid number. Please enter a whole number. !!!")
        return

    # User enters 1, but lists start at 0, so we subtract one.
    list_index_position = chosen_number - 1

    # Check 1: Is the number a valid index? (Is it too small?)
    if list_index_position < 0:
        print("\n[ERROR] !!! The number must be 1 or higher. !!!")
        return
        
    # Check 2: Is the number a valid index? (Is it too big?)
    if list_index_position >= len(the_list_of_chores):
        print(f"\n[ERROR] !!! There is no chore #{chosen_number}. Please check the list. !!!")
        return
        
    # If both checks pass, we can safely update the list item.
    the_list_of_chores[list_index_position]["status_is_done"] = True
    print(f"\n[SUCCESS] >>> Chore #{chosen_number} is now marked as finished. Great job! <<<")


# --- THE MAIN PROGRAM LOGIC ---

def run_the_chore_tracker():
    """
    This is the main loop that runs the program until the user decides to quit.
    It continually presents the menu and calls the appropriate function.
    """
    # The program should run indefinitely until the user chooses to stop.
    while True:
        print("\n----------------------------------")
        print("          MAIN MENU")
        print("----------------------------------")
        print("1. Add something new to do.")
        print("2. Look at everything I need to do.")
        print("3. Mark a task as finished.")
        print("4. STOP the program and close the list.")
        
        # Get the user's choice
        user_action = input("\nPlease type the number of your choice (1, 2, 3, or 4): ")

        if user_action == '1':
            chore_text = input("What exactly is the new chore? ")
            add_a_new_chore(chore_text)
            
        elif user_action == '2':
            show_all_chores()
            
        elif user_action == '3':
            # We show the list first so the user knows which number to choose!
            show_all_chores() 
            chore_number_to_finish = input("Which chore number did you complete? ")
            mark_chore_as_finished(chore_number_to_finish)
            
        elif user_action == '4':
            print("\n[EXITING] Thank you for using the Chore Tracker. Have a nice day!")
            break  # This keyword stops the while True loop.
            
        else:
            print("\n[WARNING] That selection was not on the menu. Please try again.")

# This line ensures the 'run_the_chore_tracker' function is the first thing 
# executed when the script is run directly. This is a common human convention.
if __name__ == "__main__":
    run_the_chore_tracker()
