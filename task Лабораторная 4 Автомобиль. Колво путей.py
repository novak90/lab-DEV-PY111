from typing import List



def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """

    table_sum = [[1 for x in range(n)] for y in range(m)]


    """ Создаем матрицу"""
    for row in range(1, m):
        for column in range(1, n):
            table_sum[row][column] = table_sum[row][column - 1] + table_sum[row - 1][column] + table_sum[row - 1][column - 1]
    return table_sum


"""Присваиваем сумму трез этих элементов  текущему элементу матрицы. 
        Этот процесс повторяется для всех элементов матрицы, кроме первой строки и первого столбца. Наконец,
        возвращается матрица table_sum. """

if __name__ == '__main__':
    paths = car_paths(5, 5)
    print(paths[-1][-1])  # 7
