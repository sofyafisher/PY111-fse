"""
Taylor series
"""
import math
from typing import Union
ERR = 0.000001

def get_value_x(x, n):
  value = ((-1) ** (n-1) * x ** (2 * n - 1)) / math.factorial(2* n - 1)
  return value

def get_value_e(x, n):
  value = (x**n)/math.factorial(n)
  return value


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    n = 0
    exx = 0
    while abs(get_value_e(x, n)) > ERR:
        exx += get_value_e(x, n)
        n += 1
        if abs(get_value_e(x, n)) <= ERR:
            return exx
    return None


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    n = 1
    sinn = 0
    while abs(get_value_x(x, n)) > ERR:
        sinn += get_value_x(x, n)
        n += 1
        if abs(get_value_x(x, n)) <= ERR:
            return sinn
    return None
