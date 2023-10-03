from src.project1.data_transform import clean_data_lower


def test_data_transform_clean_data_lower():
    """
    Test function to be use to test if the function is lower
    the input string
    """
    # Given
    input: str = "PYTHON"
    output: str = "python"

    # when
    answer: str = clean_data_lower(input)

    # then
    assert answer == output


def test_data_transform_clean_data_lower_with_space():
    """
    A test function to be test if function lower and strip
    the white spaces of the input string.
    """
    # Given
    input: str = " HELLO WORLD "
    output: str = "hello world"

    # when
    answer: str = clean_data_lower(input)

    # then
    assert answer == output
