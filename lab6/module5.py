from module6 import calculate_area, calculate_perimeter, calculate_volume

def process_rectangle(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    return {"area": area, "perimeter": perimeter}

def process_box(length, width, height):
    volume = calculate_volume(length, width, height)
    surface_area = calculate_area(length, width) * 2
    return {"volume": volume, "surface_area": surface_area}

def check_square(length, width):
    return length == width