
def ft_filter(func, list):
    """
    Filters the elements of a list based on a given function.

    Args:
        func (function): The function used to filter the list.
        list (list): The list to be filtered.

    Returns:
        list: The filtered list.
    """
    if func:
        return [i for i in list if func(i)]
    return list
