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


def main():
    with open("fib_bad.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for i in range(35):
            exe_time = perf_counter()
            val = fib_bad(i)
            exe_time = perf_counter() - exe_time
            exe_time2 = perf_counter()
            val2 = fact(i)
            exe_time2 = perf_counter() - exe_time2
            csvwriter.writerow([i, val, exe_time, val2, exe_time2])


if __name__ == "__main__":
    main()
