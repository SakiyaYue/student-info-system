import os
import re

def main():
    running = True
    while (running):
        menu()
        option = input("Option: ")
        option = re.sub(r'\D', '', option)
        if option in ['0', '1', '2', '3', '4', '5']:
            option = int(option)
            if option == 0:
                print("Exiting...")
                running = False
            elif option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                pass
            elif option == 5:
                pass

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*9 + "Menu" + "="*9)
    print()
    print("1 Create")
    print("2 Read")
    print("3 Update")
    print("4 Delete")
    print("5 Top K")
    print("0 Exit")
    print("="*22)

main()