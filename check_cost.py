import logging
import time
import psutil
from colorama import Fore, Style
from GraphsLib.GraphsLib import *


class ColorFormatter(logging.Formatter):
    """
    Class creating a colored FORMATER for logs
    """
    COLORS = {
        'DEBUG': Fore.BLUE,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.MAGENTA
    }

    def format(self, record):
        log_color = self.COLORS.get(record.levelname, Fore.WHITE)
        message = super().format(record)
        return log_color + message + Style.RESET_ALL


class PlainFormatter(logging.Formatter):
    """
    Plug, to exclude ANSI characters in the file
    """

    def format(self, record):
        return super().format(record)


def write_log(fnc_name: str, exec_time, us_memory):
    logger = logging.getLogger(fnc_name)
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColorFormatter("%(asctime)s %(message)s"))

    file_handler = logging.FileHandler(f"logs\\{fnc_name}_logs.log", mode="w")
    file_handler.setFormatter(PlainFormatter("%(asctime)s %(message)s"))

    if not logger.hasHandlers():
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    # Записываем логи
    logger.info(f"Logging information: {fnc_name}")
    logger.warning(f"average TIME spent: {exec_time} milliseconds")
    logger.error(f"average MEMORY spent: {us_memory} bytes")


def get_exec(func, *args, **kwargs):
    start_time = time.perf_counter()
    start_memory = psutil.Process().memory_info().rss

    func(*args, **kwargs)

    end_time = time.perf_counter()
    end_memory = psutil.Process().memory_info().rss

    # Вычисляем время выполнения и затраты по памяти
    execution_time = (end_time - start_time) * 1000
    memory_usage = end_memory - start_memory
    return execution_time, memory_usage


def analyze_function(extra: bool, write: bool, func, *args, **kwargs):
    """
    Function that reads average time and memory consumption
    for different algorithms

    :param extra: Use extra-graphs
    :param write: Write to console
    :param func: Func name
    :param args: Func args
    :param kwargs:
    :return:
    """
    sum_time = 0
    sum_mem = 0
    graphs = ['matrix.txt', 'matrix2.txt', 'matrix3.txt']

    for gr in graphs:
        if extra:
            graph = Graph()
            graph.extra_file(gr, *args)
        else:
            graph = Graph()
            graph.from_file(gr)

        execution_time, memory_usage = get_exec(func, graph, 1, 3)

        sum_time += execution_time
        sum_mem += memory_usage
    if write:
        write_log(func.__name__, sum_time / len(graphs),
                  sum_mem / len(graphs))

    return sum_time / len(graphs), sum_mem / len(graphs)


def better_search(func: list, extra: bool, counter: int):
    """
    A function that, for each graph, searches for the best search method

    :param func: list of search-function
    :return:
    """
    matrix = ['matrix.txt', 'matrix2.txt', 'matrix3.txt']
    for gr in matrix:

        min_time = float("inf")
        min_memory = float("inf")
        func_name_time = ''
        func_name_memory = ''

        for _ in range(counter):
            for search in func:

                if extra:
                    graph = Graph()
                    graph.extra_file(gr, 1, 3)
                else:
                    graph = Graph()
                    graph.from_file(gr)

                execution_time, memory_usage = get_exec(search, graph, 1, 3)

                if execution_time < min_time:
                    min_time = execution_time
                    func_name_time = search.__name__

                if memory_usage < min_memory:
                    min_memory = memory_usage
                    func_name_memory = search.__name__

        print(f"For {gr} graph:")

        print(f"Best time search-function is {func_name_time} :"
              f" {min_time} milliseconds")

        print(f"Best memory search-function is {func_name_memory} :"
              f" {min_memory} bytes")
        if extra:
            print("Method EXTRA")
        else:
            print("Method MINI")
        print()


def best_func(func: list, extra: bool):
    """
    Function that searches for the best functions in
    terms of time and memory used

    :param func: List of funcs
    :param extra: Use extra-graphs
    :return:
    """
    time_list = [None] * len(func)
    memory_list = [None] * len(func)
    for i, f in enumerate(func):
        time_list[i], memory_list[i] = analyze_function(extra, True, f, 1, 3)

    min_time = min(time_list)
    min_memory = min(memory_list)

    if extra:
        print("FOR EXTRA GRAPHS")
    else:
        print("FOR MINI GRAPHS")

    index = time_list.index(min_time)
    print(f"MIN TIME: {min_time}: {func[index].__name__}")
    index = memory_list.index(min_memory)
    print(f"MIN MEMORY: {min_memory}: {func[index].__name__}")
    return None


if __name__ == "__main__":
    func = [dij_alg, fld_wrsh_alg, bell_frd_alg, a_star_alg, jhn_alg]
    # best_func(func, True)
    better_search(func, False, 100)

# Сделано:
# 5ый алг (Джонсона)
# Средние в производительности
# экстра большие графы
# алг работы в доках
# цвет в логах
