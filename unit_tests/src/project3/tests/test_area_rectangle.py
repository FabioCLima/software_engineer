from src.area_rectangle import area_rectangule


def test_area_rectangle_positive_values():
    # ! Given
    base: float = 2.0
    altura: float = 6.0
    output: float = 12.0

    # ! When
    area: float = area_rectangule(base, altura)

    # ! Then
    assert area == output


def test_area_rectangle_zero():
    assert area_rectangule(0, 10) == 0
    assert area_rectangule(5, 0) == 0
    assert area_rectangule(0, 0) == 0


def test_area_rectangle_negative_values():
    # Depending on how you want the function to behave with negative inputs,
    # this test can either expect a valid area (if negative values area
    # considered valid)
    # or an assertion error (if they are not).
    assert area_rectangule(-5, 10) == -50
    assert area_rectangule(5, -10) == -50
    assert area_rectangule(-5, -10) == 50


# Test float values
def test_area_rectangle_float_values():
    assert area_rectangule(5.5, 2) == 11.0
    assert area_rectangule(3, 4.75) == 14.25
