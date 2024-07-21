import os
import re
from datetime import datetime

def get_script_path():
    return os.path.dirname(os.path.realpath(__file__))

def file_exists(file_path):
    try:
        # Validate file_path input
        if not isinstance(file_path, str):
            return False, "File path must be a string."
        if not file_path.strip():
            return False, "File path cannot be empty."
        if re.search(r"[<>*?|]", file_path):
            return False, "File path contains invalid characters (<>*?|)."
        
        if os.path.exists(file_path) and os.path.isfile(file_path):
            return True, None  # File exists and is regular
        else:
            return False, "File does not exist or is not a regular file"  # File doesn't exist or is a directory
    except OSError as e:
        # Handle OSError and return the error message
        return False, str(e)

# Test if a directory is valid and exists
def is_valid_directory(dir):
    if not isinstance(dir, str):
        return False, "Directory path must be a string."
    
    dir = dir.strip() # Input Sanitization (Remove leading and trailing whitespace)

    # Check if path is an empty string
    if not dir:
        return False, "Directory path cannot be empty."

    # Path Traversal Pattern Check (Attempts to access parent directories)
    if re.search(r"(\.\./|\.\.\\)", dir):  # Platform-agnostic
        return False, "Directory path cannot contain traversal patterns (../ or ..\\)."

    # Other Suspicious Patterns
    if re.search(r"[<>*?|]", dir):
        return False, "Directory path contains invalid characters (<>*?|)."

    if not os.path.isdir(dir):
        if os.path.exists(dir):  # Check if it exists but is not a directory
            return False, f"The path '{dir}' exists but is not a directory."
        else:
            return False, f"The directory '{dir}' does not exist."

    return True, None  # No error message since the directory is valid

def write_log(user, command, description):
    if not isinstance(user, str) or not user.strip():
        raise ValueError("User must be a non-empty string.")
    if not isinstance(command, str) or not command.strip():
        raise ValueError("Command must be a non-empty string.")
    if not isinstance(description, str):
        raise ValueError("Description must be a string.")
    
    time = datetime.now().strftime("%H:%M:%S")
    date = datetime.now().date()
    
    record = f"{date}\t\t{time}\t\t{user}\t\t{command}\t\t{description}"

    append_to_file(os.path.join(get_script_path(), "Data", "Logs.txt"), record)

def append_to_file(file_path, content): # content - String variable 
    if not isinstance(file_path, str) or not file_path.strip():
        raise ValueError("File path must be a non-empty string.")
    if not isinstance(content, str):
        raise ValueError("Content must be a string.")
    
    try:
        with open(file_path, "a") as file: # Open the file in append mode ('a'). This will append to existing content.
            file.write("\n" + content)
        print("Successfully written to file:", file_path) 

    except FileNotFoundError: # Handles the case where the file path is incorrect or inaccessible
        print("Failed to load file:", file_path) 

    except PermissionError: # Handles the case where the user doesn't have permission to write to the file
        print("Permission denied. Cannot write to:", file_path)

    except Exception as e: # A general exception handler for other unexpected errors
        print(f"An error occurred: {e}")

def __main__():
    try:
        write_log("Francois", "Rest", "Enter telescope rest mode")
    except ValueError as e:
        print(f"Validation Error: {e}")

if __name__ == '__main__':
    __main__()
