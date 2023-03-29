from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка пузырьком

    1. Пройти по всему массиву, сравнивая каждые два соседних элемента.
    2. Если элементы не находятся в нужном порядке, меняйте их местами.
    3. Повторяйте шаг 2, пока не пройдете весь массив без изменений.
    4. Повторяйте шаги 1-3, пока не отсортируете весь массив.

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    lgth = len(container)
    if lgth <= 1:
        return container
    for i in range(lgth - 1):
        marker = False
        for n in range(lgth - i - 1):
            if container[n] > container[n + 1]:
                container[n], container[n + 1] = container[n + 1], container[n]
                marker = True
        if not  marker:
            return container
