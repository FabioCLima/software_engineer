"""This module calculates the rectangule area for two given parameters
base: float, and height: float."""

from typing import Callable
from functools import wraps


def validate_inputs(func: Callable[[float, float], float]) -> \
                          Callable[[float, float], float]:
    """
    Decorator to validate input for the area_rectangule function
    """
    @wraps(func)
    def wrapper(base, height):
        # Check if both inputs are of type int or float
        if not isinstance(base, (int, float)) or not \
               isinstance(height, (int, float)):
            raise ValueError("Both base and height must be of type int or \
                             float")

        # Check if both inputs are non-negative
        if base < 0 or height < 0:
            raise ValueError("Both base and height must be non-negative.")

        # call the original function
        return func(base, height)

    return


def area_rectangule(base: float, height: float) -> float:
    """
    A simple function that computes the area of the rectangle

    Args:
        base (float): a float/int number which represents the base of the
                      rectangle.
        height (float): a float/int number which represents the height of
        the rectangle.

    Returns:
        float: The rectangle's area.
    """
    area = base * height
    return area
