from src.add_numbers import add_numbers


def test_add_numbers():
    # Given
    num1: int = 4
    num2: int = -4
    output: int = 0

    # When
    result: int = add_numbers(num1, num2)

    # Then
    assert result == output


def test_add_positive_numbers():
    # Given inputs
    num1: int = 4
    num2: int = 9
    output: int = 13
    # When
    result: int = add_numbers(num1, num2)

    # Then
    assert result == output
