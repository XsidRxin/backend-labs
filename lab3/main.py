from functions import (no_params, with_params, with_defaults, with_types,
                      with_args, with_kwargs, call_another, takes_function,
                      add_numbers, takes_function_example2,
                      takes_function_example3, inner_func, inner_func2,
                      no_lambda, simple_lambda, takes_lambda,
                      make_multiplier, make_adder, make_power)


if __name__ == '__main__':
    print("1. Function with no params:", no_params())

    print("2. Function with params:", with_params(3, 4))

    print("3. Function with defaults:", with_defaults())
    print("   With custom values:", with_defaults(2, 5))

    print("4. Function with types:", with_types(10, 3))

    print("5. Function with *args:", with_args(1, 2, 3, 4))

    print("6. Function with **kwargs:", with_kwargs(name="Bob", age=30))

    print("7. Function calling another:", call_another())

    print("8. Takes function (example 1):", takes_function(add_numbers, 5, 6))
    print("   Takes function (example 2):", takes_function_example2(lambda x: x * 3, 7))
    print("   Takes function (example 3):", takes_function_example3(lambda a, b: a ** b, 2, 3))

    print("9. Inner function (example 1):", inner_func())
    print("   Inner function (example 2):", inner_func2())

    print("10. Lambda without params:", no_lambda())

    print("11. Lambda with params:", simple_lambda(5))

    print("12. Function taking lambda:", takes_lambda(lambda x: x + 10, 5))

    mult5 = make_multiplier(5)
    print("13. Closure (multiplier):", mult5(4))

    add10 = make_adder(10)
    print("    Closure (adder):", add10(7))

    pow2 = make_power(2)
    print("    Closure (power):", pow2(8))
