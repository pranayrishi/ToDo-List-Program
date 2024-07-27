import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_men():
    print("To-Do List Application")
    print("----------------------")
    print("1. View To-Do List")
    print("2. Add To-Do Item")
    print("3. Remove To-Do Item")
    print("4. Save To-Do List")
    print("5. Load To-Do List")
    print("6. Exit")
    print("----------------------")

def view_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty")
    else: 
        for idx, item in enumerate(todo_list, start=1):
            print(f"{idx}. {item}")


def add_todo_list(todo_list):
    item = input("Enter the to-do list item")
    todo_list.append(item)
    print(f"'{item}' has been added to your todo list")

def remove_todo_item(todo_list):
    if not todo_list:
        print("Your to-do list is empty. There is nothing to remove")
        return
    try:
        item_num = int(input("Enter the number item to remove: "))
        if 1<= item_num <= len(todo_list):
            removed_item = todo_list.pop(item_num - 1)
            print(f"'{removed_item}' has been removed from the list")
        else:
            print("Invalid item number")
    except ValueError:
        print("Please enter a valid number.")

def save_todo_list(todo_list, filename="todo_list.txt"):
    with open(filename, 'w') as file:
        for item in todo_list:
            file.write(item + '\n')
    print(f"To-do has been saved to {filename}")

def load_todo_list(filename="todo_list.txt"):
    if not os.path.exists(filename):
        print(f"{filename} does not exist.")
        return []
    with open(filename, 'r') as file:
        todo_list = [line.strip() for line in file]
    print(f"To-do list has been loaded from {filename}.")
    return todo_list

def main():

    todo_list = []
    while True:
        clear_screen()
        display_men()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            view_todo_list(todo_list)
        elif choice == '2':
            add_todo_list(todo_list)
        elif choice == '3':
            remove_todo_item(todo_list)
        elif choice == '4':
            save_todo_list(todo_list)
        elif choice == '5':
            todo_list = load_todo_list()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
