# Write the class Point as outlined in the instructions
"""
For equality check for custom classes, the class should have an
__eq__ method defined to handle custom equality check.
"""
from math import sqrt


class Point:
    """
    Represents a point in a 2D space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.

    Methods:
        distance_to_origin(): Returns the distance of the point from the
        origin.
        reflect(axis: str): Reflects the point across the specified axis
        ('x' or 'y').
    """

    def __init__(self, x: float = 0.0, y: float = 0.0):
        """
        Initializes the Point with the given x and y coordinates.

        Args:
            x (float, optional): The x-coordinate of the point. Defaults to
            0.0.
            y (float, optional): The y-coordinate of the point. Defaults to
            0.0.
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"

    def distance_to_origin(self) -> float:
        """
        Calculates and returns the distance of the point from the origin.

        Returns:
            float: The Euclidean distance from the origin.
        """
        distance = sqrt((self.x)**2 + (self.y)**2)
        return distance

    def reflect(self, axis: str) -> 'Point':
        """
        Reflects the point across the specified axis.

        Args:
            axis (str): The axis of reflection ('x' or 'y').

        Returns:
            Point: A new Point object after reflection.

        Raises:
            ValueError: If the provided axis is not 'x' or 'y'.
        """
        if axis == "x":
            return Point(self.x, -1*self.y)
        elif axis == "y":
            return Point(-1*self.x, self.y)
        else:
            raise ValueError("Invalid axis for reflection. Choose 'x' or 'y'.")

    def __eq__(self, other: object) -> bool:
        """
        Determines if the current Point object is equal to another object.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if the other object is a Point and has the same
            coordinates, False otherwise.
        """
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
