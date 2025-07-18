import sys
from utils import print_main, print_satatus, print_menu
from manager import Manager

def main() -> None:
    manager = Manager()

    while not manager.user:
        print_main()
        op = input("> ")

        if op == '1':
            if manager.login():
                print_satatus("Login successful!")
                while True:
                    print_menu()
                    
                    choice = input("> ")
                    if choice == '1':
                        manager.add_task()
                    elif choice == '2':
                        pass
                    elif choice == '3':
                        pass
                    elif choice == '4':
                        pass
                    elif choice == '5':
                        break
                    else:
                        print_satatus("Xato buyruq", status='error')
                

        elif op == '2':
            manager.register()
        elif op == '3':
            sys.exit(0)
        else:
            sys.exit(1)

if __name__ == "__main__":
    main()
