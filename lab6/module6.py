from module7 import add_numbers, multiply_numbers

def calculate_area(length, width):
    return multiply_numbers(length, width)

def calculate_perimeter(length, width):
    return multiply_numbers(add_numbers(length, width), 2)

def calculate_volume(length, width, height):
    return multiply_numbers(calculate_area(length, width), height)