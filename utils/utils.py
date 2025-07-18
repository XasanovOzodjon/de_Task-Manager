def print_main() -> None:
    print('1. Sign In')
    print('2. Sign Up')
    print('3. Quit')

def is_valid_password(password):
    return len(password) >= 8 and any(char.isdigit() for char in password) and any(char.isalpha() for char in password)
