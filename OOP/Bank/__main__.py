from src.account_class import Account


def main():
    # Create an account for Alice with an initial balance of $1000
    alice_account = Account('Alice', 1000, 'password1234')

    # Check Alice's initial balance
    current_balance = alice_account.balance
    print(f"Alice's current balance: ${current_balance}")

    # Alice deposits $500
    new_balance = alice_account.deposit(500, 'password1234')
    print(f"Alice's new balance after depositing $500: ${new_balance}")

    # Alice tries to withdraw $300
    new_balance = alice_account.withdraw(300, 'password1234')
    print(f"Alice's new balance after withdrawing $300: ${new_balance}")

    # Display Alice's account details
    alice_account.show()

    # Handle exceptions when trying to withdraw more than the current balance
    try:
        alice_account.withdraw(5000, 'password1234')
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
