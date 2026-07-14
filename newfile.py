"""
---------------------------------------------------------------------------
Project Title      : Random Password Generator
Organization       : Oasis Infobyte
Domain             : Python Programming Internship
Author             : bhanu sharma
Date               : June 2026
Description        : A customizable, object-oriented password generator 
                     that creates secure, random strings based on user-defined
                     complexity constraints using the 'secrets' module.
---------------------------------------------------------------------------
"""

import sys
import string
import secrets  # Safer and more cryptographically secure than the standard 'random' module

class PasswordGenerator:
    def __init__(self):
        self.password_length = 8
        self.character_pool = ""

    def display_header(self):
        print("\n" + "="*40)
        print("    SECURE PASSWORD GENERATOR - OASIS   ")
        print("="*40)

    def get_valid_length(self):
        while True:
            try:
                length = int(input("Enter desired password length (min 4, max 50): "))
                if 4 <= length <= 50:
                    return length
                else:
                    print("Error: For safety, choose between 4 and 50.")
            except ValueError:
                print("Error: Please enter a valid integer number.")

    def build_character_pool(self):
        """Asks user for preferences and builds the character set."""
        print("\n[Configuration]: Select character types to include.")
        
        # Always include lowercase letters as a baseline safety
        self.character_pool = string.ascii_lowercase
        
        # User toggles for extra security layers
        include_upper = input("Include uppercase letters (A-Z)? (y/n): ").lower().strip()
        include_digits = input("Include numbers (0-9)? (y/n): ").lower().strip()
        include_special = input("Include special symbols (!@#$)? (y/n): ").lower().strip()

        if include_upper in ['yes', 'y']:
            self.character_pool += string.ascii_uppercase
        if include_digits in ['yes', 'y']:
            self.character_pool += string.digits
        if include_special in ['yes', 'y']:
            self.character_pool += string.punctuation

    def generate(self, length):
        """Generates a secure cryptographically random string from the pool."""
        # Using secrets.choice is a standard best-practice for security apps
        password = "".join(secrets.choice(self.character_pool) for _ in range(length))
        return password

    def run(self):
        (.display_header()
        length = self.get_valid_length()
        self.build_character_pool()
        
        # Generate and show the result
        secure_password = self.generate(length)
        
        print("\n" + "-"*40)
        print("          GENERATION SUCCESSFUL         ")
        print("-"*40)
        print(f" Generated Password : {secure_password}")
        print("="*40 + "\n")


if __22        generator.run()
        2    
            retry = input("Generate another password? (yes/no): ").lower().strip()
            if retry not in ['yes', 'y']:
                print("\n[System]: Application closed. Stay secure!")
                break
    except KeyboardInterrupt:
        print("\n\n[System]: Program exited unexpectedly.")
        sys.exit(0)
