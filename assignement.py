import random
import string
import os

# Display name and registration number
NAME = "SANWAL MEHBOOB"
REGISTRATION_NUMBER = "F2021065202"

def display_info(stage):
    print("\n" + "=" * 40)
    print(f"{NAME} - {REGISTRATION_NUMBER} ({stage})")
    print("=" * 40)

def generate_password(length=12):
    """Generate a strong password with modern security parameters."""
    if length < 12:
        raise ValueError("Password length should be at least 12 characters for strong security.")
    
    # Password criteria: Uppercase, lowercase, digits, and special characters
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()-_+=<>?/|~"
    
    # Combine all character sets
    all_chars = upper + lower + digits + special
    
    # Ensure the password includes at least one character from each set
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special),
    ]
    
    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - len(password))
    
    # Shuffle to ensure randomness
    random.shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    display_info("Before Execution")
    
    # Input password length
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 12): "))
            if length < 12:
                print("Password length must be at least 12. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Generate and display password
    password = generate_password(length)
    print(f"Generated Password: {password}")
    
    display_info("After Execution")
