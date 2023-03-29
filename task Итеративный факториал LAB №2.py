def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """

    result = 1
    """ Создаем переменную result  которая равняется  1 и доходит до значения n (включительно), умножая результат на каждой итерации. 
    На первой итерации цикла результат умножается на 1, поэтому его необходимо инициализировать равным 1"""
    if n < 0:
        raise ValueError("Только положительные числа")

    if n == 0:
        return 1

    if not isinstance(n,int):
        raise TypeError(" факториал считается  только от целого числа ")



    if n > 1:
        """ Если n большее единицы , тогда вычесляем факториал , тк факториал вычесляется только от положительных чисел"""
        for i in range(1, n + 1):
            result = result * i
        return result




if __name__ == '__main__':
    print(factorial_iterative(12))
