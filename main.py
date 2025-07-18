import sys
from utils import print_main
from manager import Manager

def main() -> None:
    manager = Manager()

    while True:
        print_main()
        op = input("> ")

        if op == '1':
            pass
        elif op == '2':
            manager.register()
        else:
            sys.exit(0)

if __name__ == "__main__":
    main()
