# Non-OOP
# Bank Version 1
# Single account


def main():
    """
    Main function that drives the banking operations.
    """
    account = {"name": "Joe", "balance": 100, "password": "soup"}

    while (action := get_user_action()) != "q":  # walrus operator
        if action == "b":
            display_balance(account)

        elif action == "d":
            account = deposit(account)

        elif action == "w":
            account = withdraw(account)

        elif action == "s":
            display_account(account)

    print("Goodbye!")


def get_user_action() -> str:
    """
    Prompt the user for an action and return the chosen action.

    Returns:
        str: The action chosen by the user.
    """
    print(
        "\n".join(
            [
                "",
                "Press b to get the balance",
                "Press d to make a deposit",
                "Press w to make a withdrawal",
                "Press s to show the account",
                "Press q to quit",
            ]
        )
    )
    return input("What do you want to do? ").lower()[0]


def display_balance(account: dict) -> None:
    """
    Display the account balance after authenticating.

    Args:
        account (dict): The account dictionary.
    """
    if authenticate(account["password"]):
        print("Your balance is:", account["balance"])


def deposit(account: dict) -> dict:
    """
    Handle deposit operation.

    Args:
        account (dict): The account dictionary.

    Returns:
        dict: The updated account dictionary.
    """
    amount = int(input("Please enter amount to deposit: "))
    if amount < 0:
        print("You cannot deposit a negative amount!")
        return account

    if authenticate(account["password"]):
        account["balance"] += amount
        print("Your new balance is:", account["balance"])

    return account


def withdraw(account: dict) -> dict:
    """
    Handle withdrawal operation.

    Args:
        account (dict): The account dictionary.

    Returns:
        dict: The updated account dictionary.
    """
    amount = int(input("Please enter the amount to withdraw: "))

    if amount < 0:
        print("You cannot withdraw a negative amount")
        return account

    if not authenticate(account["password"]):
        return account

    if amount > account["balance"]:
        print("You cannot withdraw more than you have in your account")
    else:
        account["balance"] -= amount
        print("Your new balance is:", account["balance"])

    return account


def display_account(account: dict) -> None:
    """
    Display account details.

    Args:
        account (dict): The account dictionary.
    """
    print(" Name:", account["name"])
    print(" Balance:", account["balance"])


def authenticate(correct_password: str) -> bool:
    """
    Authenticate the user by comparing input password with correct password.

    Args:
        correct_password (str): The correct password to authenticate against.

    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    return input("Please enter the password: ") == correct_password


if __name__ == "__main__":
    main()
