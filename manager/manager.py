from getpass import getpass
from models import User
from utils import is_valid_password
import json


class Manager:
    def __init__(self):
        self.user = None
        self.users = self.load_users()

    @classmethod
    def load_users(cls):
        with open('data/users.json', 'r') as jsonfile:
            try:
                return json.load(jsonfile)
            except:
                return []

    @classmethod
    def save_users(cls):
        with open('data/users.json', 'w') as jsonfile:
            json.dump([user.__dict__ for user in cls.users], jsonfile, indent=4)


    def register(self):
        name = input("name: ").strip()
        if  not name.replace("'", "").replace(" ", '').isalpha():
            print('ism xato\n')
        username = input("username: ")
        if User.check_username(username):
            print(f"{username} tanlangan.\n")
        password = getpass("password: ")
        confirm_password = getpass("confirm password: ")
        if password != confirm_password and not is_valid_password(password):
            print("password xato.\n")
        
        self.user = User(name, username, password)
        

