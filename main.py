import sys
import os
from utils import print_main
from manager import Manager
from manager import Manager

def main() -> None:
    manager = Manager()

    while True:
        print_main()
        op = input("> ")

        if op == '1':
            os.system("clear")
            print("Tizimga kirish\n")
            manager.login()
        elif op == '2':
            os.system("clear")
            print("Ro'yxatdan o'tish\n")
            manager.register()
        else:
            sys.exit(0)

if __name__ == "__main__":
    main()
