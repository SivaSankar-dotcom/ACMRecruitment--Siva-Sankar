def validate_password(password):
    # List of forbidden passwords
    forbidden_passwords = ["A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f"]
    
    if password in forbidden_passwords:
        return "Error: Password is not allowed."

    if len(password) != 8:
        return "Error: Password must be exactly 8 characters long."

    if password[0].isdigit() or not password[0].isalpha():
        return "Error: Password should not start with a number or special character."

    # Initialize flags
    has_upper = False
    has_lower = False
    has_special = False
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char in special_characters:
            has_special = True

    if not has_upper:
        return "Error: Password must contain at least one uppercase letter."
    if not has_lower:
        return "Error: Password must contain at least one lowercase letter."
    if not has_special:
        return "Error: Password must contain at least one special character."

    return "Password is valid."

def main():
    print("Password Validator")
    print("Enter a password to validate.")

    user_password = input("Password: ")
    
    result = validate_password(user_password)

    print(result)

if __name__ == "__main__":
    main()
