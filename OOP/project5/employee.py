"""Module for representing and managing employees.

This module provides a class for creating and managing employee details such
as name, salary, hire date, and operations associated with an employee like
setting their salary, giving raises, and computing monthly salary.

Typical usage example:

    emp = Employee("John", 60000)
    emp.set_salary(65000)
    monthly_pay = emp.monthly_salary()
"""

from datetime import datetime


class Employee:
    """Represents an employee with details like name, salary, and hire date.

    Attributes:
        name (str): The name of the employee.
        salary (float): The annual salary of the employee. Defaults to 0 and
            sets to 0 if a negative value is provided.
        hire_date (datetime): The date when the employee was hired, defaults
            to the current date.

    Methods:
        set_name(new_name: str): Updates the name of the employee.
        set_salary(new_salary: float): Updates the annual salary of the
        employee.
        give_raise(amount: float): Increases the employee's annual salary by
        the specified amount.
        monthly_salary(): Returns the monthly salary of the employee.
    """

    def __init__(self, name: str, salary: float = 0) -> None:
        """Initializes the Employee with the given name and salary.

        If a negative salary is provided, it defaults to 0 and prints an
        "Invalid salary" message.

        Args:
            name (str): The name of the employee.
            salary (float, optional): The annual salary of the employee.
            Defaults to 0.
    """
        self.name = name
        if salary >= 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary")

        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()

    def set_name(self, new_name: str) -> None:
        """Updates the name of the employee.

        Args:
            new_name (str): The new name to set for the employee.
    """
        self.name = new_name

    def set_salary(self, new_salary: float) -> None:
        """Updates the annual salary of the employee.

        Args:
            new_salary (float): The new annual salary for the employee.
    """
        self.salary = new_salary

    # Add a give_raise() method with raise amount as a parameter
    def give_raise(self, amount: float) -> None:
        """Increases the employee's annual salary by the specified amount.

        Args:
            amount (float): The amount by which to increase the annual salary.
    """
        self.salary += amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self) -> float:
        """Calculates and returns the monthly salary of the employee.

        Returns:
            float: The monthly salary, which is 1/12th of the annual salary.
    """
        return (self.salary)/12


if __name__ == "__main__":
    emp = Employee("Anonymous", 11700)

    # Use set_name() on emp to set the name of emp to 'Fabio Lima'
    emp.set_name('Fabio Lima')

    # Print the name of emp
    print(emp.name)

    print(emp.salary)

    # set the salary of emp to 50000
    emp.set_salary(50000)
    print(emp.salary)

    # Increase salary of emp by 1500
    emp.give_raise(1500)
    print(emp.salary)
    print()
    print(emp.hire_date)

    # Get monthly salary of emp and assign to mon_sal
    mon_sal = emp.monthly_salary()
    print(mon_sal)

    # print(dir(emp))
