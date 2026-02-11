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

def insert():
    students = []
    flag = True
    while flag:
        id = input("ID: ")
        if not id:
            break
        name = input("Name: ")
        if not name:
            break
        try:
            python = int(input("score of Python: "))
            java = int(input("score of Java: "))
            c = int(input("score of C: "))
        except:
            print("Invalid input. Please enter a integer.")
            continue
        student = {
            "id": id,
            "name": name,
            "python": python,
            "java": java,
            "c": c
        }
        students.append(student)
        inputflag = input("Continue? (y/n) :")
        flag = True if inputflag == 'y' else False
        # save(students)
        # print("Saved successfully.")

main()