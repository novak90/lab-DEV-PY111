"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """

    low = int(input())
    search_result = False
    while low < len(list) and not search_result:
        if list[low] == search_result:
            search_result = True
        else:
            low += 1

            return search_result

