# Account class
# name, password, balance will be attributes
# create, deposit, withdraw and check_balance: methods(behaviors)
# add staticmethod to the original version to performed a
# hashing using SHA-256.
# Read-Only Attributes: @property to provide a getter without a setter
# validation: attribute value meets criteria: @property decorator

import hashlib


class Account:

    def __init__(self, name: str, balance: int, password: str) -> None:
        """
        Initializes the Account with the client's name, balance and password.

        Args:
            name (str): The name of the account holder.
            balance (int): The initial balance of the account.
            password (str): The password for the account.

        >>> Joe_account = Account('Joe', 100, 'soup')
        >>> Joe_account._name
        'Joe'
        >>> Joe_account.balance
        100
        """

        self._name = name
        self._balance = int(balance)
        self._password = self._hash_password(password)

    # * Está sendo usada como uma função utilitária pra "encriptar"
    # * o atributo de instância password, não mudando o estado da mesma
    @staticmethod
    def _hash_password(password: str) -> str:
        """Hashes a password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

    @property
    def balance(self) -> int:
        """
        Gets the balance of the account.
        Returns:
            int: balance of the account

        >>> account = Account('Alice', 150, 'password123')
        >>> account.balance
        150
        """
        return self._balance

    def deposit(self, amount_to_deposit: int, password: str) -> int:
        """
        Deposits an amount into the account.

        Args:
            amount_to_deposit (int): Amount to be deposited.
            password (str): Account password for verification.

        Returns:
            int: Updated account balance.

        Raises:
            ValueError: If incorrect password or negative deposit amount.

        >>> account = Account('Bob', 50, 'password321')
        >>> account.deposit(50, 'password321')
        100
        """
        if self._hash_password(password) != self._password:
            raise ValueError("Incorrect password")
        if amount_to_deposit < 0:
            raise ValueError("Cannot deposit a negative amount")

        self._balance += amount_to_deposit
        return self._balance

    def withdraw(self, amount_to_withdraw: int, password: str) -> int:
        """
        Withdraws an amount from the account.
        Args:
            amount_to_withdraw (int): Amount to be withdrawn.
            password (str): Account password for verification.
        Returns:
            int: Updated account balance.
        Raises:
            ValueError: If incorrect password, negative withdrawal amount, or
            insufficient funds.
        """
        if self._hash_password(password) != self._password:
            raise ValueError("Incorrect password")
        if amount_to_withdraw < 0:
            raise ValueError("Cannot withdraw a negative amount")
        if amount_to_withdraw > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount_to_withdraw
        return self._balance

    def show(self) -> None:
        """
        Displays the account details.
        Note: For security reasons, the password is not shown.
        """
        print('       Name:', self._name)
        print('       Balance:', self._balance)
        print('       Password: *****')
        print()
