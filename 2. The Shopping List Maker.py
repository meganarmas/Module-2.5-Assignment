#Objective: The aim of this assignment is to create a program that helps users make a shopping list.
# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a function to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.
# Note: The goal of this is to be a program. 
# The recommendation is to use a while loop that will allow the user to 
# continue to add, remove, and print off their shopping list until they decide to 
# "quit", also known as breaking the loop.

shopping_lists = ['bananas', 'apples', 'cereal', 'avocados']

def manage_list():
   while True:
    print("Would you like to view list, add items, or removed items?")
    print("1. View Shopping List")
    print("2. Add Items")
    print("3. Remove Items")
    print("4. Quit")
    choice = input("Enter choice: ")

    if choice == '1':
            print("Current List")
            for shopping_list in shopping_lists:
                print(shopping_list)
    elif choice == '2':
            new_item = input("Enter what to add to the shopping list: ")
            shopping_lists.append(new_item)
            print(f"{new_item} has been added to the shopping list!")
    elif choice == '3':
            remove_item = input("Enter what to remove from the shopping list: ")
            if remove_item in shopping_list:
               shopping_lists.remove(remove_item)
               print(f"{remove_item} has been removed to the shopping list!")
            else:
               print(f"{remove_item} was not found on the shopping list.")
    elif choice == '4':
            print("Exiting Shopping List. Thanks!")
            break
    else:
         print("Invalid numbers. Please restart.")

manage_list()
