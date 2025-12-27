from exceptions import (throws_exception1, throws_exception2, single_handler,
                       with_finally, multiple_handlers1, multiple_handlers2,
                       multiple_handlers3, raise_example, use_custom_exception,
                       demo_exception1, demo_exception2, demo_exception3)

def run_all():
    print("1. Testing throws_exception1:")
    try:
        throws_exception1()
    except ZeroDivisionError:
        print("   ZeroDivisionError caught in main")

    print("2. Testing throws_exception2:")
    try:
        throws_exception2()
    except IndexError:
        print("   IndexError caught in main")

    print("3. Testing single_handler:")
    result = single_handler()
    print("   Result:", result)

    print("4. Testing with_finally:")
    result = with_finally()
    print("   Result:", result)

    print("5. Testing multiple_handlers1:")
    result = multiple_handlers1()
    print("   Result:", result)

    print("6. Testing multiple_handlers2:")
    result = multiple_handlers2()
    print("   Result:", result)

    print("7. Testing multiple_handlers3:")
    result = multiple_handlers3()
    print("   Result:", result)

    print("8. Testing raise_example:")
    try:
        raise_example()
    except ValueError:
        print("   ValueError caught in main")

    print("9. Testing use_custom_exception:")
    result = use_custom_exception()
    print("   Result:", result)

    print("10. Testing demo_exception1:")
    result = demo_exception1()
    print("    Result:", result)

    print("11. Testing demo_exception2:")
    result = demo_exception2()
    print("    Result:", result)

    print("12. Testing demo_exception3:")
    result = demo_exception3()
    print("    Result:", result)


if __name__ == '__main__':
    run_all()
