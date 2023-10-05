import matplotlib.pyplot as plt
import numpy as np

import matplotlib as mpl
import csv
from random import shuffle
from time import perf_counter


def fact(n):
    if n > 0:
        return n*fact(n-1)
    else:
        return 1


def fib_bad(n):
    if n > 1:
        return fib_bad(n-1) + fib_bad(n-2)
    else:
        return 1


def fib_good(n):
    a = 0
    b = 0
    c = 1
    for i in range(n):
        a = c + b
        b = c
        c = a
    return c


def main():
    data_fib_good = []
    data_fib_bad = []
    data_fact = []
    data_sort = []
    data_num = []
    for x in range(900):
        data_num.append(x)
    for x in range(150):
        print(x)
        for i in range(900):
            if x == 0:
                list = []
                for z in range(i):
                    list.append(z)
                shuffle(list)
                exe_time = perf_counter()
                val = fact(i)
                exe_time = perf_counter() - exe_time
                data_fact.append(exe_time)
                """
                exe_time2 = perf_counter()
                val2 = fib_bad(i)
                exe_time2 = perf_counter() - exe_time2
                data_fib_bad.append(exe_time2)
                """
                exe_time3 = perf_counter()
                val3 = fib_good(i)
                exe_time3 = perf_counter() - exe_time3
                data_fib_good.append(exe_time3)
                exe_time4 = perf_counter()
                list.sort()
                exe_time4 = perf_counter() - exe_time4
                data_sort.append(exe_time4)
            else:
                list = []
                for z in range(i):
                    list.append(z)
                shuffle(list)
                exe_time = perf_counter()
                val = fact(i)
                exe_time = perf_counter() - exe_time
                data_fact[i] = (exe_time + data_fact[i])/(x+1)
                """
                exe_time2 = perf_counter()
                val2 = fib_bad(i)
                exe_time2 = perf_counter() - exe_time2
                data_fib_bad[i] = (exe_time2 + data_fib_bad[i])/(x+1)
                """
                exe_time3 = perf_counter()
                val3 = fib_good(i)
                exe_time3 = perf_counter() - exe_time3
                data_fib_good[i] = (exe_time3 + data_fib_good[i])/(x+1)
                exe_time4 = perf_counter()
                list.sort()
                exe_time4 = perf_counter() - exe_time4
                data_sort[i] = (exe_time4 + data_sort[i])/(x+1)
    fig, ax = plt.subplots()
    ax.plot(data_num, data_fib_good, label="Fib_Good")
    """
    ax.plot(data_num, data_fib_bad, label="Fib_Bad")
    """
    ax.plot(data_num, data_fact, label="Fact")
    ax.plot(data_num, data_sort, label="Sort")
    ax.legend()
    plt.ylim(0, 0.000001)
    plt.show()
    plt.savefig("Plot.PDF", format="pdf", bbox_inches="tight")

    '''''
    with open("data.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(35):
            list = []
            for x in range(i):
                list.append(x)
            shuffle(list)
            exe_time = perf_counter()
            val = fact(i)
            exe_time = perf_counter() - exe_time
            exe_time2 = perf_counter()
            val2 = fib_bad(i)
            exe_time2 = perf_counter() - exe_time2
            exe_time3 = perf_counter()
            val3 = fib_good(i)
            exe_time3 = perf_counter() - exe_time3
            exe_time4 = perf_counter()
            list.sort()
            exe_time4 = perf_counter() - exe_time4
            csvwriter.writerow([i, exe_time, exe_time2, exe_time3, exe_time4])
'''''

if __name__ == "__main__":
    main()