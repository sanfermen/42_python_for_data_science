import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    This function truncate a 2D array based on 2 integer indices.
    The function also checks if the input parameters are of the
    correct type and if all lists in the 2D list have the same length.

    Parameters:
    family (list): A 2D list of integers or floats.
    start (int): The start index for slicing the list.
    end (int): The end index for slicing the list.

    Returns:
    list: A new 2D list that includes the elements from the start index up to,
            but not including, the end index.
            If an error occurs, an empty string is returned.
    """
    try:
        if not isinstance(family, list):
            raise AssertionError("The first argument must be a list.")
        if not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("The second and third arguments must be int")
        if not all(len(list) == len(family[0]) for list in family):
            raise AssertionError("The lists must have the same length.")
        print(f"My shape is : {np.array(family).shape}")
        new = family[start:end]
        print(f"My new shape is : {np.array(new).shape}")
        return new
    except AssertionError as e:
        print(e)
        return ""
