"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    min_ = arr[0]
    for index, value in enumerate(arr):
        if value < min_:
            min_ = value
            ind = index
    return ind


    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    print(arr)
    return -1
