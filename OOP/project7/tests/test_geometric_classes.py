# ! test_geometric_classes.py - Module
from __future__ import annotations
from src.geometric_classes import Point, Rectangle
from math import sqrt


def test_point_class_instantiation():
    # Given: Two coordinates for the new point
    x1 = 3.0
    y1 = 4.0
    p1 = Point(x1, y1)

    # When:
    p = Point(3.0, 4.0)

    # Then:
    assert p.x == p1.x
    assert p.y == p1.y


def test_point_class_equality():
    # Given:
    x1 = 3.0
    y1 = 4.0
    p1 = Point(x1, y1)

    # When
    p = Point(3.0, 4.0)

    # Then:
    assert p == p1


"""
# first version of test
def test_point_class_falls_in_rectangle():
    # * Given: Three object's Point, where two define a rectangle and one is
    # * the test point. The test return True if the test point falls within
    # * the rectangle and False otherwise.

    lower_left = Point(0, 0)
    upper_right = Point(10, 10)

    # 1. Test point inside rectangle
    # the return of the test should be True
    test_point_inside = Point(5, 5)
    assert test_point_inside.falls_inside_rectangle(
        lower_left, upper_right)

    # 2. Test point outside rectangle
    test_point_outside = Point(15, 15)
    assert not test_point_outside.falls_inside_rectangle(
        lower_left, upper_right)

    # 3. Test point on the edge of the rectangle (e.g., on the right edge)
    test_point_on_edge = Point(10, 5)
    assert test_point_on_edge.falls_inside_rectangle(
        lower_left, upper_right)
"""


def test_point_class_falls_inside_rectangle():
    """
    Test the functionality of the method falls_inside_rectangle of the Point
    class.
    """

    # Given: A Rectangle object defined by two Points (lower_left and
    # upper_right)
    lower_left = Point(0, 0)
    upper_right = Point(10, 10)
    rectangle = Rectangle(lower_left, upper_right)

    # 1. Test point inside rectangle
    test_point_inside = Point(5, 5)
    assert test_point_inside.falls_inside_rectangle(rectangle)

    # 2. Test point outside rectangle
    test_point_outside = Point(15, 15)
    assert not test_point_outside.falls_inside_rectangle(rectangle)

    # 3. Test point on the edge of the rectangle (e.g., on the right edge)
    test_point_on_edge = Point(10, 5)
    assert test_point_on_edge.falls_inside_rectangle(rectangle)


def test_distance_method():
    """
    This test verifies the calculation of the distance between
    two Point objects.
    """
    # 1. Test the distance is always positive
    # Given: two Points.
    p1: Point = Point(3, 4)
    p2: Point = Point(5, 6)

    # When: perform the distance calculation between the two
    # given points
    distance = p1.distance(p2)

    # Then: The result should be a positive value
    assert distance > 0

    # 2. Test the distance against an expected value
    # Given: two Points.
    p1 = Point(3, 4)
    p2 = Point(5, 6)

    # When: calculating the distance between the two points
    distance = p1.distance(p2)

    # Then: The result should match the expected value
    expected_distance = sqrt((5 - 3) ** 2 + (6 - 4) ** 2)
    assert distance == expected_distance

    # 3. Test the distance when both points are the same
    # Given: two identical Points
    p3 = Point(2, 2)
    p4 = Point(2, 2)

    # When: calculating the distance between the two identical points
    distance_same_points = p3.distance(p4)

    # Then: The distance should be 0
    assert distance_same_points == 0

    # 3. Test the distance where one point is at the origin
    # Given: a Point at the origin and another Point
    p5 = Point(0, 0)
    p6 = Point(3, 4)

    # When: calculating the distance between the origin and the point
    distance_from_origin = p5.distance(p6)

    # Then: The result should match the hypotenuse of a 3-4-5 triangle
    assert distance_from_origin == 5.0


def test_rectangle_class_instantiation():
    """
    Comparing the lowleft and upright attributes of the rectangle object to
    the expect Point objects.
    """

    # Given: Two Points for the Rectangle's lowerleft and upright corners
    lowleft: Point = Point(3, 4)
    upright: Point = Point(4, 5)

    # When: Instantiate a new rectangle object
    rectangle: Rectangle = Rectangle(lowleft, upright)

    # Then: The Rectangle's attributes should match the given Points
    assert rectangle.lowleft == lowleft
    assert rectangle.upright == upright


def test_rectangle_class_area_calculation():
    """
    Testing the calculation of rectangle's area object given the lowleft
    and upright corners.
    """

    # Given: Two Points for the Rectangle's lowleft and upright corners
    lowleft = Point(2, 4)
    upright = Point(6, 6)
    rectangle = Rectangle(lowleft, upright)

    # When: Calculating the expected area using the difference in x and y
    # coordinates between the lowleft and upright points.
    width = upright.x - lowleft.x
    height = upright.y - lowleft.y
    expected_area = width * height

    # Calculate the rectangle's area using the method from the Rectangle class.
    calculated_area = rectangle.area()

    # Then: The Rectangle's area should match the expected value
    assert expected_area == calculated_area
