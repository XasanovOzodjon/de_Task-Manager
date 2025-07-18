from getpass import getpass
from models import User
from utils import is_valid_password
import json
import os
from hashlib import sha256


class Manager:
    def __init__(self):
        self.user = None
        self.users = self.load_users()

    @staticmethod
    def check_username(users, username):
        for user in users:
            if user["username"] == username:
                return True
        return False

    @staticmethod
    def load_users():
        try:
            with open('data/users.json', 'r') as jsonfile:
                return json.load(jsonfile)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []

    def save_users(self):
        with open('data/users.json', 'w') as jsonfile:
            json.dump(self.users, jsonfile, indent=4)

    def register(self):
        name = input("name: ").strip()
        if not name.replace("'", "").replace(" ", '').isalpha():
            print('Ism noto‘g‘ri\n')
            return

        username = input("username: ").strip()
        if self.check_username(self.users, username):
            os.system("clear")
            print(f"{username} allaqachon band.\n")
            return

        password = getpass("password: ").strip()
        confirm_password = getpass("confirm password: ").strip()

        if password != confirm_password:
            os.system("clear")
            print("Parollar mos emas.\n")
            return

        if not is_valid_password(password):
            os.system("clear")
            print("Parol talabga javob bermaydi.\n")
            return

        self.user = User(name, username, password)
        self.users.append(self.user.__dict__)
        self.save_users()
        os.system("clear")
        print(f"{username} muvaffaqiyatli ro‘yxatdan o‘tdi.")

    def login(self):
        username = input("username: ").strip()
        password = getpass("password: ").strip()

        for user in self.users:
            if user.get("username") == username and user.get("pasword") == sha256(password.encode()).hexdigest():
                self.user = User(user["name"], user["username"], user["pasword"])
                os.system("clear")
                print(f"{username} tizimga muvaffaqiyatli kirdi.")
                return

        os.system("clear")
        print("Username yoki parol xato.")

