from hashlib import sha256
from termcolor import colored

def print_main() -> None:
    print('1. Sign In')
    print('2. Sign Up')
    print('3. Quit')
    
def print_menu():
    print('1. Create Task')
    print('2. View Tasks')
    print('3. Do Task')
    print('4. View Not Doing Tasks')
    print('5. Logout')

def is_valid_password(password):
    return len(password) >= 8

def is_valid_name(name):
    return name.replace("'", "").replace(" ", '').isalpha()

def make_password(password):
    return sha256(password.encode()).hexdigest()

def print_satatus(text, status='success'):
    status_map = {
        'error': 'red',
        'success': 'green'
    }
    print(colored(text, status_map[status]))
    