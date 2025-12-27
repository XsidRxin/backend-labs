from module3 import calculate_diagonal, calculate_circle_area, calculate_sphere_volume, process_with_math
import locale

def format_number_locale(number):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return locale.format_string("%.2f", number)

def get_locale_info():
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return locale.getlocale()

def compare_numbers_locale(num1, num2):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    formatted1 = locale.format_string("%.2f", num1)
    formatted2 = locale.format_string("%.2f", num2)
    return {"num1": formatted1, "num2": formatted2}

def convert_currency(amount):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    return locale.currency(amount, symbol=True)