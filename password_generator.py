import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_characters=True):
    """
    Generates a random password based on the given criteria.

    Args:
        length (int): Length of the password. Default is 12.
        include_uppercase (bool): Include uppercase letters in the password. Default is True.
        include_numbers (bool): Include numbers in the password. Default is True.
        include_special_characters (bool): Include special characters in the password. Default is True.

    Returns:
        str: Generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    special_characters = string.punctuation if include_special_characters else ""

    # Combine all selected pools
    all_characters = lowercase + uppercase + numbers + special_characters

    if not all_characters:
        raise ValueError("No character sets selected for password generation.")

    # Ensure at least one character from each selected pool is included
    password = [
        random.choice(lowercase),
        random.choice(uppercase) if include_uppercase else "",
        random.choice(numbers) if include_numbers else "",
        random.choice(special_characters) if include_special_characters else ""
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    print("Random Password Generator")
    try:
        length = int(input("Enter the desired password length (default 12): ") or 12)
        include_uppercase = input("Include uppercase letters? (y/n, default y): ").lower() != 'n'
        include_numbers = input("Include numbers? (y/n, default y): ").lower() != 'n'
        include_special_characters = input("Include special characters? (y/n, default y): ").lower() != 'n'

        password = generate_password(
            length=length,
            include_uppercase=include_uppercase,
            include_numbers=include_numbers,
            include_special_characters=include_special_characters
        )
        print("\nGenerated Password:", password)
    except ValueError as e:
        print("Error:", e)
