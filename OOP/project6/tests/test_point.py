from src.point_class import Point


def test_point_class_initialization_with_defaults():
    # When: A Point object is created without specific values
    pt1 = Point()

    # Then: The point object should have its x and y attributes set to default
    # values
    assert pt1.x == 0.0
    assert pt1.y == 0.0


def test_point_initialization_with_values():
    # Given: Specific x and values for initialization
    x_val, y_val = 3.0, 4.0

    # When: A Point object is created with those values
    p = Point(x_val, y_val)

    # Then: The Point object should have its x and y attributes set to those
    # values
    assert p.x == x_val
    assert p.y == y_val


def test_point_distance_to_origin():
    # Given: two coordinates for point initialization
    x_val, y_val = 3.0, 4.0

    # When: A Point object is created with those values
    p = Point(x_val, y_val)
    distance_to_origin = p.distance_to_origin()

    # Then: The distance to origin for the given values should be 5
    assert distance_to_origin == 5


def test_point_reflect_y_axis():
    """
    Test the reflection of a point across the y-axis.

    Given a point with specific x and y coordinates, when reflected across
    the y-axis, the x-coordinate should be negated while the y-coordinate
    remains unchanged.

    For example:
    A point with coordinates (3.0, 4.0) should transform to (-3.0, 4.0)
    after reflection across the y-axis.
    """

    # Given: two coordinates for point initialization and the "axis"
    # for the reflection operation:
    x_val, y_val = 3.0, 4.0
    axis: str = "y"

    # When: A reflection method is called
    p = Point(x_val, y_val)
    answer = p.reflect(axis)

    # Then: Should the x coordinate of the point multiply *-1
    assert answer == Point(-3.0, 4.0)
