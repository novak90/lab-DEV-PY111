from typing import Union
import networkx as nx


def stairway_path(graph: nx.DiGraph) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param graph: Взвешенный направленный граф NetworkX, по которому надо рассчитать стоимости кратчайших путей
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    _, coasts = nx.dijkstra_predecessor_and_distance(graph, 0)
    return list(coasts.values())[
        -1]


def get_graph(path):
    """ используем модуль NX для создания графа взвешенного направленный граф на основе заданного списка  """
    graph = nx.DiGraph()
    queue = list(path)[::-1]
    graph.add_weighted_edges_from([(0, 1, queue.pop())])
    n = 1
    while queue:
        """ прописываем массив значений для графа,Цикл while перебирает 
        оставшиеся элементы в списке очереди, который содержит веса в
         обратном порядке. Внутри цикла код извлекает последний элемент из списка очереди и присваивает его переменной веса. """
        weight = queue.pop()
        graph.add_weighted_edges_from([(n, n + 1, weight), (n - 1, n + 1, weight)])
        n += 1
    return graph
""" Наконец, цикл увеличивает переменную n на 1, чтобы создать ребра между следующей парой узлов в графе.
 Цикл while продолжается до тех пор, пока в списке очереди не останется элементов."""

if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = get_graph(stairway)
    print(stairway_path(stairway_graph))  # 72

if __name__ == '__main__':
    stairway = (5, 11, 43, 2, 23, 43, 22, 12, 6, 8)
    stairway_graph = ...  # TODO записать взвешенный граф, а лучше написать функцию, которая формирует граф по стоимости ступеней
    print(stairway_path(stairway_graph))  # 72
