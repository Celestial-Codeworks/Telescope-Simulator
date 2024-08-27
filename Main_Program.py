import Calculations as C, File_Handling as FH, Telescope_Movement as TM, re, getpass

USER, PASSWORD = 'f', 'f'

COMMAND_DESCRIPTIONS = {
    "Telescope Control": "Display menu responsible for telescope control functions. ",
    "Configure Settings": "Display menu responsible for configuration settings. ",
    "Coordinate System": "Display menu responsible for coordinate calculations and conversions. ",
    "Display Data": "Display menu responsible for displaying system info. ",
    "Exit": "Exit the RTOS program. ",
    "Point to AltAz": "Point telescope to specific Alt (altitude) & Az (azimuth) degrees. ",
    "Point To RaDec": "Point telescope to specific Ra (right ascension) & Dec (declination) values. ",
    "Tracking": "Initiate tracking process to track a celestial object. ",
    "Rest Mode": "Move telescope to rest mode. ",
    "Back": "Go back to the previous menu. ",
    "Change Telescope Location": "Change physical location values of telescope (Latitude, Longitude, Elevation). ",
    "Change Data Location": "Change the location where the telescope frequency data is stored. ",
    "Convert Alt & Az to Ra & Dec": "Convert Alt (altitude) & Az (azimuth) degrees to Ra (right ascension) & Dec (declination) values.",
    "Convert Ra & Dec to Alt & Az": "Convert Ra (right ascension) & Dec (declination) values to Alt (altitude) & Az (azimuth) degrees.",
    "Display location": "Display location using IP, GPS, and the last stored location in the configuration file. ",
    "Display Telescope Logs": "Display log files created by software. ",
    "Display All Commands & Descriptions": "Display list of all commands in program and their descriptions. ",
    "Display Available Celestial Objects": "Display list of all celestial objects that are in a certain radius from ra (right ascension) & dec (declination) values. "
}

MAIN_MENU = ["1. Telescope Control",
            "2. Configure Settings",
            "3. Coordinate System",
            "4. Display Data",
            "5. Exit"]

TELESCOPE_CONTROL_MENU = ["1. Point To AltAz",
                        "2. Point To RaDec",
                        "3. Tracking",
                        "4. Rest Mode",
                        "5. back"]

CONFIG_SETTINGS_MENU = ["1. Change Telescope Location",
                        "2. Change Data Location",
                        "3. back"]

COORDINATE_MENU = ["1. Convert Alt & Az to Ra & Dec",
                "2. Convert Ra & Dec to Alt & Az",
                "3. back"]

DISPLAY_SYS_DATA_MENU = ["1. Display Location",
                        "2. Display Telescope Logs",
                        "3. Display All Commands & Descriptions",
                        "4. Display Available Celestial Objects",
                        "5. back"]

def display_menu(menu_num):
    print("\n")

    if menu_num == 0: # Main Menu
        print("\n")
        print("*******************************")
        print("   Radio Telescope Control     ")
        print("*******************************")

        for i in MAIN_MENU:
            print(i)
    elif menu_num == 1: # Telescope Control Menu
        for i in TELESCOPE_CONTROL_MENU:
            print(i)
    elif menu_num == 2: # Configure Settings Menu
        for i in CONFIG_SETTINGS_MENU:
            print(i)
    elif menu_num == 3: # Coordinate Menu
        for i in COORDINATE_MENU:
            print(i)
    elif menu_num == 4: # Display System Data Menu
        for i in DISPLAY_SYS_DATA_MENU:
            print(i)

def telescope_control_functions(choice):
    if choice == 1: # Point to altaz 
        alt, az = get_valid_alt_az()

        # ADD FUNCTIONALITY TO MOVE TELESCOPE HERE
    elif choice == 2: # Point to radec
        ra, dec = get_valid_ra_dec()

        # ADD FUNCTIONALITY TO MOVE TELESCOPE HERE
    elif choice == 3: # Tracking
        celestial_code = get_valid_celestial_code()
        print("\n")

        TM.track_celestial_object(celestial_code)
    elif choice == 4: # Rest mode
        # ADD FUNCTIONALITY TO MAKE TELESCOPE ENTER REST MODE
        pass
    
    elif choice == 5: # Back to main menu, do not check this value
        pass
    
    else:
        print("Invalid input, please enter a number next to the command you want to execute.")

def configure_settings_functions(choice):
    if choice == 1: # Change Telescope Location
        pass
    
    elif choice == 2: # Data store location
        pass
    
    elif choice == 3: # Back to main menu, do not check this value
        pass
    
    else: 
        print("Invalid input, please enter a number next to the command you want to execute.")

def coordinate_functions(choice):
    if choice == 1: # Convert AltAz to Ra & Dec
        alt, az = get_valid_alt_az()
        ra, dec = C.convert_altaz_to_radec(alt, az)
        print(f"Altaz converted to ra and dec:  RA: {ra}  DEC: {dec}")
            
    elif choice == 2: # Convert Ra & Dec to AltAZ
        ra, dec = get_valid_ra_dec()
        alt, az = C.convert_radec_to_altaz(ra, dec)
        print(f"radec converted to alt and az:  ALT: {alt}  AZ: {az}")
        
    elif choice == 3: # Back to main menu, do not check this value
        pass
    
    else: 
        print("Invalid input, please enter a number next to the command you want to execute.")

def display_sys_data_functions(choice):
    if choice == 1: # Display location
        print("(Latiude, Longitude, Elevation)")
        print(f"IP: {C.get_location_and_elevation('ip')}")
        print(f"Last Saved: {C.get_location_and_elevation('stored')}")
        
    elif choice == 2: # Display telescope logs
        FH.display_logs()
        
    elif choice == 3: # Display commands & descriptions
        print("\nAvailable commands: \n")

        for command, description in COMMAND_DESCRIPTIONS.items():
            print(f"{command}: {description}")
            
    elif choice == 4: # List celestial objects
        ra, dec = get_valid_ra_dec()
        C.list_celestial_objects_in_region(ra, dec, radius = 0.1)
            
    elif choice == 5: # Back to main menu, do not check this value
        pass
    
    else: 
        print("Invalid input, please enter a number next to the command you want to execute.")

def alt_az_input_validation(alt, az):
    # alt validation
    if not isinstance(alt, (float, int)):
        raise ValueError("Alt (Altitude) must be a number")
    if not (-75 <= alt <= 75):
        raise ValueError("Alt (Altitude) must be between -90 and 90 degrees")
    
    # az validation
    if not isinstance(az, (float, int)):
        raise ValueError("Az (Azimuth) must be a number")
    if not (-340 <= alt <= 340):
        raise ValueError("Az (Azimuth) must be between -90 and 90 degrees")
    
    return True # If user input passes validation

def get_valid_alt_az():
    while True:
        try:
            alt = float(input("Enter Alt (Altitude) degrees (-90 to 90): ")) # Input alt
            az = float(input("Enter Az (Azimuth) degrees (0 to 360): ")) # Input az

            alt_az_input_validation(alt, az) # Validation for alt and az
            print("Valid Alt/Az input!") # For debuging
            return alt, az  # Return the validated values
        except ValueError as e:
            print(f"Validation error: {e}. Please try again.\n")

def ra_dec_input_validation(ra, dec):
    # Define regex patterns for ra and dec in the specific format
    ra_pattern = r"^\d{1,2}h\d{1,2}m\d{1,2}(\.\d+)?s$"
    dec_pattern = r"^[+-]?\d{1,2}d\d{1,2}m\d{1,2}(\.\d+)?s$"

    # ra validate
    if not re.match(ra_pattern, ra):
        raise ValueError("RA (Right Ascension) must be in the format 'hhmmss', e.g., '00h42m30s'.")
    
    # dec validate
    if not re.match(dec_pattern, dec):
        raise ValueError("Dec (Declination) must be in the format '+/-ddmmss', e.g., '+41d12m00s'.")

    return True  # If user input passes validation

def get_valid_ra_dec():
    while True:
        try:
            ra = input("Enter RA (Right Ascension) value (e.g., '00h42m30s'): ") # Input ra
            dec = input("Enter Dec (Declination) value (e.g., '+41d12m00s'): ") # Input dec

            ra_dec_input_validation(ra, dec) # Validation for ra and dec
            print("Valid RA/Dec input!") # For debuging
            return ra, dec  # Return the validated values
        except ValueError as e:
            print(f"Validation error: {e}. Please try again.\n")

def celestial_code_input_validation(code):
    # Check if the code is alphanumeric and not empty
    if not code.isalnum():
        raise ValueError("The code must be alphanumeric.")
    # Check the length of the code
    if len(code) < 3:
        raise ValueError("The code must be at least 3 characters long.")

    return True  # If user input passes validation

def get_valid_celestial_code():
    while True:
        try:
            code = input("\nEnter the code of the celestial object that you would like to track: ")
            celestial_code_input_validation(code) # Validation for celestial_code
            print("Valid code input!") # For debuging
            return code  # Return the validated code
        except ValueError as e:
            print(f"Validation error: {e}. Please try again.\n")

def __main__():
    b_flag = False

    # Check login details
    while b_flag == False:
        user = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ") # Hiddes password, does not echo the password as the user types.

        if (USER == user) & (PASSWORD == password):
            b_flag = True
        else: print("Incorrect login!!!\n")

    print("\n")

    while True:
        display_menu(0) # Display main menu
        choice = int(input("\nEnter your choice: ")) # Input to select menu
        display_menu(choice)

        if choice == 1: # Telescope control
            tc_choice = int(input("\nEnter your choice: "))
            telescope_control_functions(tc_choice)
        elif choice == 2: # Configure settings
            cs_choice = int(input("\nEnter your choice: "))
            configure_settings_functions(cs_choice)
        elif choice == 3: # Coordinate system
            c_choice = int(input("\nEnter your choice: "))
            coordinate_functions(c_choice)
        elif choice == 4: # Display system data
            sd_choice = int(input("\nEnter your choice: "))
            display_sys_data_functions(sd_choice)
        elif choice == 5: # Exit
            exit()
        else:
            print("Invalid input, please enter a number next to the command you want to execute.")
        
        print("\n")

if __name__ == '__main__':
    __main__()