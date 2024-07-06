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
    or contains only one element, it returns that element.
    """
    ln = len(list_of_integers)
    if not list_of_integers:
        return None
    if ln == 1:
        return list_of_integers[0]
    mid = ln // 2
    if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and\
            (mid == ln - 1 or
                list_of_integers[mid] >= list_of_integers[mid + 1]):
        return list_of_integers[mid]
    elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
