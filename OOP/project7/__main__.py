from __future__ import annotations
from src.geometric_classes import Point, Rectangle
from random import randint


def main():
    # Creating a rectangle object using randint
    rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                          Point(randint(10, 19), randint(10, 19)))

    print(f"Rectangle Coordinates: \n"
          f"({rectangle.lowleft.x}, {rectangle.lowleft.y}), and \n"
          f"({rectangle.upright.x}, {rectangle.upright.y})\n")

    try:
        x, y = map(float, input("Enter X and Y (X, Y): ").split())
        user_point = Point(x, y)

        inside_rectangle = user_point.falls_inside_rectangle(rectangle)
        print(f"Your point was inside rectangle: {inside_rectangle}")

        user_area = float(input("Guess rectangle area: "))
        difference = rectangle.area() - user_area
        print(f"Your area guessed was off by: {difference}")

    except ValueError:
        print("Invalid input. Please provide valid numbers.")


if __name__ == "__main__":
    main()
