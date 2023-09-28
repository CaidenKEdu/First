import csv
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
    with open("data.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(35):
            exe_time = perf_counter()
            val = fact(i)
            exe_time = perf_counter() - exe_time
            exe_time2 = perf_counter()
            val2 = fib_bad(i)
            exe_time2 = perf_counter() - exe_time2
            exe_time3 = perf_counter()
            val3 = fib_good(i)
            exe_time3 = perf_counter() - exe_time3
            csvwriter.writerow([i, val, exe_time, val2, exe_time2, val3, exe_time3])

if __name__ == "__main__":
    main()