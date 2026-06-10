# Program Name: Assignment1.py
# Course: IT3883/Section W01
# Student Name: Khalil Jackson
# Assignment Number: Lab 1
# Due Date: 06/12/2026
# Purpose: This program prints a board that allows you to append, clear, and display an input buffer


running = True
buffer = ""

while running:
    print("\nType the option number you would like to execute"
          "\n\nOption 1: Append data to the input buffer\nOption 2: Clear the input buffer\nOption 3: Display the input buffer\nOption 4: Exit the program")
    option = input("\nEnter option: ")

    if option == "1":
        buffer += input("Enter what you would like to append: ")
    elif option == "2":
        buffer = ""
    elif option == "3":
        print(buffer)
    elif option == "4":
        running = False
    else:
        print("Enter valid option: ")


print("Thank you!")


