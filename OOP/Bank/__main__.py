# Main program for controlling a Bank made up of Accounts

# Bring in all the code of the Bank class
from src.bank_class import Bank


def main():
    """Main function to interact with the bank operations."""
    # Create an instance of the Bank
    bank_instance = Bank()

    # Create two test accounts
    joes_account_number = bank_instance.create_account("Joe", 100, "JoesPassword")
    print(f"Joe's account number is: {joes_account_number}")

    marys_account_number = bank_instance.create_account("Mary", 12345, "MarysPassword")

    print(f"Mary's account number is: {marys_account_number}")

    while True:
        print("\nOptions:")
        print("b - Get an account balance")
        print("c - Close an account")
        print("d - Make a deposit")
        print("i - Get bank information")
        print("o - Open a new account")
        print("s - Show all accounts")
        print("w - Make a withdrawal")
        print("q - Quit")

        action = input("What do you want to do? ").lower().strip()

        if action == "b":
            bank_instance.balance()
        elif action == "c":
            bank_instance.close_account()
        elif action == "d":
            bank_instance.deposit()
        elif action == "i":
            bank_instance.bank_info()
        elif action == "o":
            bank_instance.open_account()
        elif action == "s":
            bank_instance.show()
        elif action == "w":
            bank_instance.withdraw()
        elif action == "q":
            break
        else:
            print("Sorry, that was not a valid action. Please try again.")

    print("Done")


if __name__ == "__main__":
    main()
