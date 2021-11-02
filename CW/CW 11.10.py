import time

num = 1  # операция присваивания переменной
# num значения 1

# 1num = 1 # syntaxError

numf = 1.2

# print(type(numf))

# print(r"Hello\tworld\n")

# print("hello"[-2:])

# print("1¹²²³⁴⁴".isdigit())

# qwe = [4, 5, 3, 1]
# qwe.sort()
# b = sorted(qwe, key=lambda x: -x);
# print(b)

import time


def time_of_function(func):
    def wrapped(*args):
        start_time = time.time_ns()
        func()
        print(time.time_ns() - start_time)
    return wrapped


@time_of_function
def foo():
    for i in range(1000000):
        pass


foo()