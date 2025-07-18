from hashlib import sha256

class User:


    def __init__(self, name, username, password):
        hashed_password = sha256(password.encode()).hexdigest()

        self.user_id = 1
        self.name = name
        self.username = username
        self.pasword = hashed_password
