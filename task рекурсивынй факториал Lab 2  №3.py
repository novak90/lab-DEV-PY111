def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    if not isinstance(n,int):
        raise TypeError(" факториал считается  только от целого числа ")
    if n < 0:
        raise ValueError("Только положительные числа")
    """Проверка на положительность числа"""
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n-1)

""" Это будет рекурсивный шаг нашего факториала"""

if __name__ == '__main__':
    print(factorial_recursive(5))
