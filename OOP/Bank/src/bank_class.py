# bank_class.py - manager object
"""
The bank can be modeled as an object that manages other (account) objects,
known as an object manager object - It is an object that maintains a list
or dictionary of managed objects (typically of a single class) and calls
methods of those objects.
"""
from account_class import Account


class Bank:
    """
    Represents a bank, which manages multiple accounts.

    A bank is an object manager that maintains a dictionary of managed account
    objects.
    Each account is identified by a unique ID generated by the bank.

    Attributes:
        account_id_counter (int): Class variable to keep track of the next
        available account ID.
        accounts_dict (dict of int to Account): Dictionary of accounts managed
        by the bank, where the key is the account ID and the value is the
        corresponding account object.

    Example:
        >>> bank = Bank()
        >>> account_id = bank.create_account('Alice', 1000, 'password1234')
        >>> bank.accounts_dict[account_id].balance
        1000
    """

    account_id_counter = 0

    def __init__(self) -> None:
        """
        Initializes a new Bank object with an empty accounts dictionary.
        """
        self.accounts_dict = {}

    def create_account(self, client_name: str, start_amount: int, password: str) -> int:
        """
        Creates a new account, adds it to the bank's accounts dictionary, and
        returns its ID.

        Args:
            client_name (str): Name of the client.
            start_amount (int): Initial deposit amount.
            password (str): Account password.

        Returns:
            int: The ID of the newly created account.

        Example:
            >>> bank = Bank()
            >>> account_id = bank.create_account('Bob', 500, 'password5678')
            >>> bank.accounts_dict[account_id].balance
            500
        """
        Bank.account_id_counter += 1
        new_account = Account(client_name, start_amount, password)
        self.accounts_dict[Bank.account_id_counter] = new_account
        return Bank.account_id_counter

    def open_account(self) -> None:
        """
        Interactively creates a new account by collecting user input.
        The created account is added to the bank's accounts dictionary
        and its ID is displayed.

        Example:
            >>> bank = Bank()
            >>> bank.open_account()
            *** Open Account ***
            What is the name for the new user account? Alice
            What is the starting balance for this account? 1000
            What password would you want to use for this account? password1234
        """
        print("*** Open Account ***")
        username = input("What is the name for the new user account? ")
        user_starting_amount = input(
            "What is the starting balance for this\
                                      account? "
        )
        user_starting_amount = int(user_starting_amount)
        user_password = input(
            "What password would you want to use for this\
                              account? "
        )

        user_account_number = self.create_account(
            username, user_starting_amount, user_password
        )

        print(f"Account number for {username} is: {user_account_number}")
        print()

    def close_account(self) -> None:
        """
        Closes a user's account based on the provided account number and
        password.
        The balance of the account is returned to the user before closing.
        """
        print("*** Close Account ***")

        try:
            user_account_number = int(input("What is your account number? "))
            user_password = input("What is your password? ")

            # Validate if account exists
            if user_account_number not in self.accounts_dict:
                print("Account number does not exist.")
                return

            account = self.accounts_dict[user_account_number]

            # Validate password
            if account._hash_password(user_password) != account._password:
                print("Incorrect password.")
                return

            balance = account.balance
            print(
                f"You had ${balance} in your account, which is being\
                  returned to you."
            )

            # Remove user's account from the dictionary of accounts
            del self.accounts_dict[user_account_number]
            print("Your account is now closed.")
        except ValueError:
            print("Please enter a valid account number.")

    def balance(self) -> None:
        """Get the balance of a user's account."""
        print("*** Get Balance ***")
        try:
            prompt = "Please enter your account number: "
            user_account_number = int(input(prompt))
            user_password = input("Please enter the password: ")

            # Validate if account exists
            if user_account_number not in self.accounts_dict:
                print("Account number does not exist.")
                return

            account = self.accounts_dict[user_account_number]
            # Validate password
            if account._hash_password(user_password) != account._password:
                print("Incorrect password.")
                return

            print("Your balance is:", account.balance)
        except ValueError:
            print("Please enter a valid account number.")

    def deposit(self) -> None:
        """Handle deposit action for a user's account."""
        print("*** Deposit ***")
        try:
            account_num = int(input("Please enter the account number: "))
            deposit_amount = int(input("Please enter amount to deposit: "))
            user_password = input("Please enter the password: ")
            account = self.accounts_dict[account_num]
            account.deposit(deposit_amount, user_password)
            print("Your new balance is:", account.balance)
        except KeyError:
            print("Account number does not exist.")
        except ValueError as e:
            print(f"Error: {e}")

    def show(self) -> None:
        """Display details for all the accounts."""
        print("*** Show ***")
        for account_num, account in self.accounts_dict.items():
            print("   Account number:", account_num)
            account.show()

    def withdraw(self) -> None:
        """Handle withdrawal action for a user's account."""
        print("*** Withdraw ***")
        try:
            prompt = "Please enter your account number: "
            user_account_number = int(input(prompt))
            user_amount = int(input("Please enter the amount to withdraw: "))
            user_password = input("Please enter the password: ")
            account = self.accounts_dict[user_account_number]
            account.withdraw(user_amount, user_password)
            print("Withdrew:", user_amount)
            print("Your new balance is:", account.balance)
        except KeyError:
            print("Account number does not exist.")
        except ValueError as e:
            print(f"Error: {e}")

    def bank_info(self) -> None:
        """Display general bank information."""
        print("Hours: 9 to 5")
        print("Address: 123 Main Street, Anytown, USA")
        print("Phone:  (650) 555-1212")
        print("We currently have", len(self.accounts_dict), "account(s) open.")
