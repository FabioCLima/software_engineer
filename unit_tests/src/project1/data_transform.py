"""
This module takes a string as input and clean it: remove the white spaces,
and lower the characteres.
"""


def clean_data_lower(input: str) -> str:
    """
    This function takes a string and remove the white spaces and lower
    its characters.
    Args:
        string (str): string to be processed

    Returns:
        str: the processed string
    """
    result: str = input.lower().strip()
    return result
