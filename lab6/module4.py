from module5 import process_rectangle, process_box, check_square
import random

def get_random_dimension():
    return random.randint(1, 100)

def generate_random_rectangle():
    length = get_random_dimension()
    width = get_random_dimension()
    return process_rectangle(length, width)

def generate_random_box():
    length = get_random_dimension()
    width = get_random_dimension()
    height = random.uniform(1, 50)
    return process_box(length, width, height)

def shuffle_dimensions(dimensions):
    shuffled = dimensions.copy()
    random.shuffle(shuffled)
    return shuffled