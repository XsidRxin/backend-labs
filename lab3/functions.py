def no_params():
    return "function with no params"


def with_params(x, y):
    return x + y


def with_defaults(a=10, b=20):
    return a * b


def with_types(x: int, y: int) -> int:
    return x - y


def with_args(*numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


def with_kwargs(**info):
    result = ""
    for key in info:
        result = result + key + "=" + str(info[key]) + " "
    return result


def call_another():
    value = add_numbers(7, 8)
    return value


def add_numbers(a, b):
    return a + b


def takes_function(func, a, b):
    return func(a, b)


def takes_function_example2(func, value):
    return func(value)


def takes_function_example3(operation, x, y):
    return operation(x, y)


def inner_func():
    def helper(x):
        return x * 2
    value = helper(5)
    return value


def inner_func2():
    def double(n):
        return n + n
    def triple(n):
        return n * 3
    return double(4) + triple(4)


no_lambda = lambda: "lambda without params"


simple_lambda = lambda x: x * 2


def takes_lambda(func, n):
    return func(n)


def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier


def make_adder(n):
    def adder(x):
        return x + n
    return adder


def make_power(base):
    def power(exp):
        return base ** exp
    return power
