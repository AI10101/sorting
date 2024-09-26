import random
import time
import matplotlib.pyplot as plt # type: ignore
from algorithms import *





def plot(plot_arr_size, plot_time, algorithm_name):
    plt.plot(plot_arr_size, plot_time, label = algorithm_name)

    plt.xlabel('array size')
    plt.ylabel('time taken')
    plt.title(algorithm_name)

    plt.draw()


def test(algorithm, arr_size = 10, max_arr_size = 200, iterations = 10000, step = 10):
    plot_arr_size = []
    plot_time = []

    arr = list(range(arr_size))
    random.shuffle(arr)
    algorithm.sort(arr, len(arr) - 1)

    print(algorithm.__name__ + ' test case:')
    print(arr)

    while arr_size <= max_arr_size:
        duration = 0
        arr = list(range(arr_size))

        for _ in range(iterations):
            random.shuffle(arr)
            start = time.time()
            algorithm.sort(arr, len(arr) - 1)
            end = time.time()
            duration += end - start

        plot_arr_size.append(arr_size)
        plot_time.append(duration)

        arr_size += step

    plot(plot_arr_size, plot_time, algorithm.__name__)


if __name__ == '__main__':
    test(bubble_sort)
    test(selection_sort)
    test(insertion_sort)
    test(merge_sort)
    test(quick_sort)
    test(python_sort)

    plt.legend()
    plt.show()
