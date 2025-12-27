class CustomError(Exception):
    pass

class ValidationError(Exception):
    pass

class NegativeNumberError(Exception):
    pass

def throws_exception1():
    x = 10
    y = 0
    return x / y

def throws_exception2():
    numbers = [1, 2, 3]
    return numbers[10]

def single_handler():
    try:
        value = int("not a number")
    except Exception:
        return "Error caught"
    return value

def with_finally():
    try:
        result = 100 / 10
        return result
    except Exception:
        return None
    finally:
        print("Finally block executed")

def multiple_handlers1():
    try:
        nums = [1, 2, 3]
        result = nums[5]
    except ValueError:
        return "ValueError"
    except IndexError:
        return "IndexError caught"
    except TypeError:
        return "TypeError"
    return result


def multiple_handlers2():
    try:
        x = "hello"
        y = x + 5
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError caught"
    except ZeroDivisionError:
        return "ZeroDivisionError"
    return y

def multiple_handlers3():
    try:
        value = 10 / 0
    except ValueError:
        return "ValueError"
    except TypeError:
        return "TypeError"
    except ZeroDivisionError:
        return "ZeroDivisionError caught"
    return value

def raise_example():
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

def custom_exception1():
    pass

def custom_exception2():
    pass

def custom_exception3():
    pass

def use_custom_exception():
    try:
        status = "active"
        if status != "active":
            raise CustomError("Status is not active")
        return "OK"
    except CustomError:
        return "Custom error caught"

def demo_exception1():
    try:
        result = 50 / 5
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero"

def demo_exception2():
    try:
        nums = [10, 20, 30]
        return nums[0]
    except IndexError:
        return "Index out of range"

def demo_exception3():
    try:
        value = int("123")
        return value
    except ValueError:
        return "Invalid integer"
