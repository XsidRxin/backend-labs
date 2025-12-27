from module2 import format_number_locale, get_locale_info, compare_numbers_locale, convert_currency
from decimal import Decimal, ROUND_HALF_UP
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    name: str
    price: Decimal
    quantity: int
    sku: str = ""
    description: str = ""
    
    def __post_init__(self):
        if isinstance(self.price, (int, float, str)):
            self.price = Decimal(str(self.price))


@dataclass
class Order:
    order_id: int
    customer_name: str
    products: list
    total: Decimal
    order_date: str = ""
    status: str = "pending"
    
    def __post_init__(self):
        if isinstance(self.total, (int, float, str)):
            self.total = Decimal(str(self.total))


@dataclass
class Invoice:
    invoice_id: str
    order: Order
    tax_amount: Decimal
    final_total: Decimal
    issued_date: str = ""
    
    def __post_init__(self):
        if isinstance(self.tax_amount, (int, float, str)):
            self.tax_amount = Decimal(str(self.tax_amount))
        if isinstance(self.final_total, (int, float, str)):
            self.final_total = Decimal(str(self.final_total))


def calculate_price(quantity, unit_price):
    result = Decimal(str(quantity)) * Decimal(str(unit_price))
    return result.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def calculate_discount(original_price, discount_percent):
    original = Decimal(str(original_price))
    discount = Decimal(str(discount_percent))
    discounted = original * (1 - discount / 100)
    return discounted.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def calculate_tax(price, tax_rate):
    price_decimal = Decimal(str(price))
    tax = Decimal(str(tax_rate))
    with_tax = price_decimal * (1 + tax / 100)
    return with_tax.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

def financial_report(items):
    total = Decimal('0')
    for item in items:
        total += Decimal(str(item))
    return total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)


def process_single_product(product: Product) -> dict:
    if not isinstance(product, Product):
        raise TypeError("Parameter must be a Product instance")
    
    total_value = product.price * product.quantity
    return {
        "product_name": product.name,
        "unit_price": float(product.price),
        "quantity": product.quantity,
        "total_value": float(total_value)
    }


def process_product_list(products: list) -> dict:
    if not isinstance(products, list) or not all(isinstance(p, Product) for p in products):
        raise TypeError("Parameter must be a list of Product instances")
    
    total_items = sum(p.quantity for p in products)
    total_cost = sum(float(p.price * p.quantity) for p in products)
    
    return {
        "total_items": total_items,
        "total_cost": total_cost,
        "number_of_products": len(products)
    }


def process_product_dict(products_dict: dict) -> dict:
    if not isinstance(products_dict, dict):
        raise TypeError("Parameter must be a dictionary")
    
    result = {}
    total = Decimal('0')
    
    for key, product in products_dict.items():
        if isinstance(product, Product):
            value = product.price * product.quantity
            result[key] = {
                "name": product.name,
                "value": float(value)
            }
            total += value
    
    result["inventory_total"] = float(total)
    return result


def modify_product_price(product: Product, new_price: float) -> Product:
    product.price = Decimal(str(new_price))
    return product


def create_product_from_params(name: str, price: float, quantity: int, sku: str = "", description: str = "") -> Product:
    return Product(name=name, price=Decimal(str(price)), quantity=quantity, sku=sku, description=description)


def process_order_with_products(order: Order) -> dict:
    if not isinstance(order, Order):
        raise TypeError("Parameter must be an Order instance")
    
    return {
        "order_id": order.order_id,
        "customer": order.customer_name,
        "total": float(order.total),
        "status": order.status,
        "product_count": len(order.products) if order.products else 0
    }


def create_invoice_from_order(order: Order, tax_rate: float) -> Invoice:
    tax = order.total * Decimal(str(tax_rate / 100))
    final_total = order.total + tax
    return Invoice(
        invoice_id=f"INV-{order.order_id:05d}",
        order=order,
        tax_amount=tax.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        final_total=final_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP),
        issued_date=datetime.now().strftime("%Y-%m-%d")
    )


def update_order_total(order: Order, new_total: float) -> Order:
    order.total = Decimal(str(new_total))
    return order


def process_multiple_orders(orders: list) -> dict:
    if not isinstance(orders, list):
        raise TypeError("Parameter must be a list of Order instances")
    
    result = {}
    grand_total = Decimal('0')
    
    for i, order in enumerate(orders, 1):
        if isinstance(order, Order):
            result[f"order{i}"] = {
                "customer": order.customer_name,
                "total": float(order.total),
                "date": order.order_date
            }
            grand_total += order.total
    
    result["grand_total"] = float(grand_total)
    return result


def generate_random_product() -> Product:
    import random
    names = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"]
    prices = [999.99, 29.99, 79.99, 299.99, 149.99]
    quantities = [1, 5, 10, 3, 2]
    
    idx = random.randint(0, 4)
    return Product(
        name=names[idx],
        price=Decimal(str(prices[idx])),
        quantity=quantities[idx]
    )