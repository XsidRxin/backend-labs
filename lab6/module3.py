from module4 import generate_random_rectangle, generate_random_box, shuffle_dimensions
import math

def calculate_diagonal(length, width):
    return math.sqrt(length**2 + width**2)

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def process_with_math(length, width):
    diagonal = calculate_diagonal(length, width)
    circle = calculate_circle_area(length)
    return {"diagonal": diagonal, "circle_area": circle}