from handlers import (
    parse_input,
    add_contact,
    change_number,
    get_phone_by_name,
    show_all_contacts,
    add_birthday,
    show_birthday,
    birthdays,
)
from storage import load_data, save_data


def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "stop"]:
            save_data(book)
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(args, book))
        
        elif command == "change":
            print(change_number(args, book))
        
        elif command == "phone":
            print(get_phone_by_name(args, book))
        
        elif command == "all":
            print(show_all_contacts(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))
        
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
