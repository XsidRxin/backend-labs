from module7 import create_all_objects, Point
from module1 import (
    calculate_price, calculate_discount, calculate_tax, financial_report,
    process_single_product, process_product_list, process_product_dict,
    modify_product_price, create_product_from_params, process_order_with_products,
    create_invoice_from_order, update_order_total, process_multiple_orders,
    generate_random_product, Product, Order, Invoice
)
from module2 import format_number_locale, get_locale_info, compare_numbers_locale, convert_currency
from module3 import calculate_diagonal, calculate_circle_area, calculate_sphere_volume, process_with_math
from module4 import generate_random_rectangle, generate_random_box, shuffle_dimensions
from module5 import process_rectangle, process_box, check_square
from decimal import Decimal


def run_all_demonstrations():
    
    print("=" * 60)
    print("MODULES DEMONSTRATION")
    print("=" * 60)
    
    print("\n--- Import Tree Structure ---")
    print("Module chain: module1 -> module2 -> module3 -> module4 -> module5 -> module6 -> module7")
    rect = process_rectangle(5, 10)
    print(f"Rectangle result: {rect}")
    
    print("\n--- Random Module Functions ---")
    dimensions = [10, 20, 30, 40]
    shuffled = shuffle_dimensions(dimensions)
    print(f"Original: {dimensions}")
    print(f"Shuffled: {shuffled}")
    
    rect_random = generate_random_rectangle()
    print(f"Random rectangle: {rect_random}")
    
    box_random = generate_random_box()
    print(f"Random box: {box_random}")
    
    print("\n--- Math Module Functions ---")
    diagonal = calculate_diagonal(3, 4)
    print(f"Diagonal of 3x4: {diagonal:.2f}")
    
    circle_area = calculate_circle_area(5)
    print(f"Circle area (r=5): {circle_area:.2f}")
    
    sphere_vol = calculate_sphere_volume(3)
    print(f"Sphere volume (r=3): {sphere_vol:.2f}")
    
    result = process_with_math(6, 8)
    print(f"Math operations: {result}")
    
    print("\n--- Locale Module Functions ---")
    formatted = format_number_locale(1234.5678)
    print(f"Formatted number: {formatted}")
    
    locale_info = get_locale_info()
    print(f"Locale info: {locale_info}")
    
    compared = compare_numbers_locale(100.456, 200.789)
    print(f"Compared numbers: {compared}")
    
    currency = convert_currency(99.99)
    print(f"Currency format: {currency}")
    
    print("\n--- Decimal Module Functions ---")
    price = calculate_price(5, 29.99)
    print(f"Price calculation: {price}")
    
    discounted = calculate_discount(100, 15)
    print(f"Discounted price: {discounted}")
    
    with_tax = calculate_tax(100, 10)
    print(f"Price with tax: {with_tax}")
    
    items = [10.5, 20.3, 15.7]
    total = financial_report(items)
    print(f"Financial total: {total}")
    
    print("\n--- Data Classes ---")
    product1 = create_product_from_params("Laptop", 999.99, 2)
    print(f"Single product: {process_single_product(product1)}")
    
    product2 = create_product_from_params("Mouse", 29.99, 5)
    product3 = create_product_from_params("Keyboard", 89.99, 3)
    products = [product1, product2, product3]
    print(f"Product list: {process_product_list(products)}")
    
    product_dict = {
        "laptop": product1,
        "mouse": product2,
        "keyboard": product3
    }
    print(f"Product dict: {process_product_dict(product_dict)}")
    
    original_price = float(product1.price)
    modified = modify_product_price(product1, 899.99)
    print(f"Price modification: ${original_price} -> ${modified.price}")
    
    new_product = create_product_from_params("Monitor", 299.99, 1)
    print(f"Created from params: {new_product}")
    
    order = Order(1, "John Doe", [product2, product3], Decimal('419.92'))
    order_result = process_order_with_products(order)
    print(f"Order: ID={order_result['order_id']}, Total=${order_result['total']}")
    
    invoice = create_invoice_from_order(order, 10)
    print(f"Invoice: ID={invoice.invoice_id}, Total=${invoice.final_total}")
    
    updated_order = update_order_total(order, 469.92)
    print(f"Updated total: ${updated_order.total}")
    
    random_product = generate_random_product()
    print(f"Random product: {random_product.name}")
    
    orders = [
        order,
        Order(2, "Jane Smith", [product1], Decimal('1999.98'), "2025-12-26")
    ]
    summary = process_multiple_orders(orders)
    print(f"Orders summary: {summary}")


if __name__ == "__main__":
    print("\n")
    
    objects = create_all_objects()
    print("=== Classes Demonstration ===")
    print(f"Person: {objects['person'].name}, Age {objects['person'].age}")
    print(f"Car: {objects['car'].get_brand()}")
    objects['car'].set_brand("Honda")
    print(f"Car after update: {objects['car'].get_brand()}")
    print(f"Bank balance: ${objects['account'].balance}")
    objects['account'].deposit(500)
    print(f"Bank after deposit: ${objects['account'].balance}")
    
    p1 = objects['point']
    p2 = Point(5, 12)
    print(f"Points: {p1} + {p2} = {p1 + p2}")
    print(f"Animals: {objects['dog'].speak()}, {objects['cat'].speak()}")
    print(f"Circle area: {objects['circle'].area():.2f}")
    print(f"Movement: {objects['bird'].move()}, {objects['fish'].move()}")
    print(f"Vehicle: {objects['vehicle'].brand}")
    print(f"Temperature: {objects['temperature']}")
    
    print("\n")
    run_all_demonstrations()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETED")
    print("=" * 60)
