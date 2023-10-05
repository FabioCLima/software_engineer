# ***********************************************************************
# ! By importing annotations from __future__, we can use the class name
# ! directly in type hints within the class itself.
# ***********************************************************************


from __future__ import annotations
from typing import Any
from math import sqrt


class Point:
    """
    Represents a point in a 2D space.

    Attributes:
        x (float): The x-coordinate of the point.
        y (float): The y-coordinate of the point.

    >>> p = Point(2, 3)
    >>> str(p)
    'Point(2, 3)'
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initializes a Point with the given x and y coordinates.

        >>> p = Point(1, 2)
        >>> p.x, p.y
        (1, 2)
        """
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """
        Returns a string representation of the Point object.

        >>> p = Point(4, 5)
        >>> str(p)
        'Point(4, 5)'
        """
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other: Any) -> bool:
        """
        Determines if the current Point object is equal to another object.

        >>> p1 = Point(1, 2)
        >>> p2 = Point(1, 2)
        >>> p1 == p2
        True
        >>> p3 = Point(3, 4)
        >>> p1 == p3
        False
        """
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def falls_inside_rectangle(self, rectangle: Rectangle) -> bool:
        """
        Checks if the point falls inside a given rectangle.

        >>> rect = Rectangle(Point(0, 0), Point(5, 5))
        >>> p = Point(3, 3)
        >>> p.falls_inside_rectangle(rect)
        True
        >>> p2 = Point(6, 6)
        >>> p2.falls_inside_rectangle(rect)
        False
        """
        return (
            rectangle.lowleft.x <= self.x <= rectangle.upright.x
            and rectangle.lowleft.y <= self.y <= rectangle.upright.y
        )

    def distance(self, p2: Point) -> float:
        """
        Calculates the distance between the current point and a given point.

        >>> p1 = Point(0, 0)
        >>> p2 = Point(3, 4)
        >>> p1.distance(p2)
        5.0
        """
        return sqrt((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2)


class Rectangle:
    """
    Represents a rectangle in a 2D space.

    A rectangle is defined by two points: the lower left corner (`lowleft`)
    and the upper right corner (`upright`).

    Attributes:
        lowleft (Point): The lower left corner of the rectangle.
        upright (Point): The upper right corner of the rectangle.

    >>> r = Rectangle(Point(0, 0), Point(2, 3))
    >>> str(r)
    'Rectangle(Point(0, 0), Point(2, 3))'
    >>> r.area()
    6.0
    """

    def __init__(self, lowleft: Point, upright: Point) -> None:
        """
        Initializes a Rectangle with the given lowleft and upright corners.

        >>> r = Rectangle(Point(1, 2), Point(3, 4))
        >>> r.lowleft.x, r.lowleft.y, r.upright.x, r.upright.y
        (1, 2, 3, 4)
        """
        self.lowleft = lowleft
        self.upright = upright

    def __str__(self) -> str:
        """
        Returns a string representation of the Rectangle object.

        >>> r = Rectangle(Point(1, 1), Point(4, 4))
        >>> str(r)
        'Rectangle(Point(1, 1), Point(4, 4))'
        """
        return f"Rectangle({self.lowleft}, {self.upright})"

    def area(self) -> float:
        """
        Calculates and returns the area of the rectangle.

        >>> r = Rectangle(Point(0, 0), Point(2, 3))
        >>> r.area()
        6.0
        """
        return (self.upright.x - self.lowleft.x) * (self.upright.y - self.lowleft.y)
