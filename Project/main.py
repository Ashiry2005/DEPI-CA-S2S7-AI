"""
Hospital Attendance System - Command Line Interface

This module serves as the main entry point for the hospital's daily attendance system. 
It provides an interactive command-line menu where staff members can identify themselves, 
input their specific details based on their role, and log their attendance.

Dependencies:
    Requires the 'models.py' file containing the definitions for:
    Staff, Doctor, Nurse, Receptionist, Engineer, and Manager classes.
"""

from staff import Staff, Doctor, Nurse, Receptionist, Engineer, Manager


def attended(staff_member, attendance_list):
    """
    Extracts the core details from a staff member object and logs them into the attendance list.

    This function takes a staff member object (which could be any of the subclasses 
    like Doctor, Nurse, etc.), creates a dictionary of their common attributes 
    (id, name, and position), and appends this dictionary to the provided list.

    Args:
        staff_member (Staff): An instance of the Staff class (or one of its subclasses) 
                              representing the person logging in.
        attendance_list (list): The list acting as the database to store all attendance records.

    Returns:
        None
    """
    # Create a dictionary containing the required attributes
    record = {
        "id": staff_member.id,
        "name": staff_member.name,
        "position": staff_member.position
    }
    
    # Append the dictionary to the main attendance list
    attendance_list.append(record)
    
    # Provide feedback to the user
    print(f"\n[SUCCESS] Attendance recorded for {staff_member.name} ({staff_member.position}).\n")


def main():
    """
    Runs the main application loop for the Command Line Interface (CLI).

    This function initializes an empty list to store the daily attendance records 
    and presents the user with a looping menu. Depending on the user's choice, it can:
    1. Prompt the user for their details, instantiate the appropriate class based 
       on their job title, and log their attendance.
    2. Display all attendance records logged during the current session.
    3. Exit the application.
    """
    # Initialize an empty list to hold the dictionaries of attendees
    daily_attendance = []
    
    print("=======================================")
    print("      Hospital Attendance System       ")
    print("=======================================")
    
    # Start the continuous user interface loop
    while True:
        print("1. Log Attendance")
        print("2. View Current Attendance List")
        print("3. Exit")
        
        # Capture the user's menu selection
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            try:
                # Gather common details required by the base Staff class
                emp_id = int(input("\nEnter your ID (numeric): "))
                name = input("Enter your Name: ")
                position = input("Enter your Position (Doctor/Nurse/Receptionist/Engineer/Manager/Other): ").strip()
                
                # Convert position to lowercase to make the if-statements case-insensitive
                position_lower = position.lower()
                
                # Check the position to ask for role-specific details and instantiate the correct class
                if position_lower == "doctor":
                    specialty = input("Enter your Specialty: ")
                    staff_user = Doctor(emp_id, name, position, specialty)
                    
                elif position_lower == "nurse":
                    department = input("Enter your Department: ")
                    staff_user = Nurse(emp_id, name, position, department)
                    
                elif position_lower == "receptionist":
                    shift = input("Enter your Shift (e.g., Morning/Night): ")
                    staff_user = Receptionist(emp_id, name, position, shift)
                    
                elif position_lower == "engineer":
                    field = input("Enter your Field (e.g., maintenance, installation, sales): ")
                    staff_user = Engineer(emp_id, name, position, field)
                    
                elif position_lower == "manager":
                    department = input("Enter your Department: ")
                    staff_user = Manager(emp_id, name, position, department)
                    
                else:
                    # If the role isn't specifically defined, fall back to the generic Staff class
                    staff_user = Staff(emp_id, name, position)

                # Pass the newly created object and the tracking list to the attended function
                attended(staff_user, daily_attendance)
                
            except ValueError:
                # Handle the case where the user inputs letters/symbols instead of a number for the ID
                print("\n[ERROR] Invalid ID format! Please enter a numeric ID.\n")
                
        elif choice == '2':
            # Display all logged records
            print("\n--- Today's Attendance Records ---")
            if not daily_attendance:
                print("No one has logged attendance yet.")
            else:
                for entry in daily_attendance:
                    print(entry)
            print("----------------------------------\n")
            
        elif choice == '3':
            # Break the loop to close the program
            print("Exiting system. Have a great day!")
            break
            
        else:
            # Handle invalid menu selections
            print("\n[ERROR] Invalid choice. Please select 1, 2, or 3.\n")


# Ensure the main function only runs if this file is executed directly (not imported as a module)
if __name__ == "__main__":
    main()