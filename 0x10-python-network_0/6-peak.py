#!/usr/bin/python3
"""finds the peaks"""


def find_peak(list_of_integers):
    """
    This function finds the peak element in a list of integers
    using a divide and conquer approach.
    The peak element is defined as an element that is greater
    than its neighboring elements.

    Parameters:
    list_of_integers (List[int]): A list of integers.

    Returns:
    int: The peak element in the list. If the list is empty
    or contains only one element, it returns that element."""
    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        mid = len(list_of_integers) // 2
        if (list_of_integers[mid] > list_of_integers[mid - 1] and
                list_of_integers[mid] > list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif list_of_integers[mid] > list_of_integers[mid - 1]:
            return find_peak(list_of_integers[mid:])
        else:
            return find_peak(list_of_integers[:mid])
