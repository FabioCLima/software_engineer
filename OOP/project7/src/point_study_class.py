from __future__ import annotations
import math


class Point:
    """
    Represents a point in two-dimensional geometric coodinates

    >>> p_0 = Point(0, 0)
    >>> p_1 = Point(3, 4)
    >>> p_0.calculate_distance(p_1)
    5.0
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Initialize the position of a new point.The x and y coordinates can be
        specified. If they are not, the point defaults to the origin.
        Args:
            x (float): x-coordinate
            y (float): y-coordinate
        """
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        """
        Move the point to a new location in 2D space.

        Args:
            x (float): x-coordinate
            y (float): y-coordinate
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        Reset the point back to the geometric origin: 0, 0
        """
        self.move(0, 0)

    def calculate_distance(self, other: Point) -> float:
        """
        Distance between the point 1 and another provided point2: other
        Args:
            other (Point): [description]

        Returns:
            float: [description]
        """
        print("Calculating the distance between p1 and other point! ...")
        return math.hypot(self.x - other.x, self.y - other.y)


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(0, 0)
    p1.reset()
    p2.move(5, 0)
    print(p2.calculate_distance(p1))
    assert p2.calculate_distance(p1) == p1.calculate_distance(p2)
    p1.move(3, 4)
    print(p1.calculate_distance(p2))
    print(p1.calculate_distance(p1))
    point = Point(3, 5)
    print(point.x, point.y)
    help(Point)
