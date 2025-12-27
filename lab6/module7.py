def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def subtract_numbers(a, b):
    return a - b


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Car:
    def __init__(self, brand, model):
        self._brand = brand
        self.model = model
    
    def get_brand(self):
        return self._brand
    
    def set_brand(self, brand):
        self._brand = brand


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        return f"{self.name} says: {self.sound}"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof!")


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Meow!")


class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2


class Movable:
    def move(self):
        return "Moving"


class Bird(Movable):
    def move(self):
        return "Bird is flying"


class Fish(Movable):
    def move(self):
        return "Fish is swimming"


class Engine:
    def __init__(self, type_):
        self.type = type_


class Vehicle:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    def __repr__(self):
        return f"{self.celsius}°C = {self.to_fahrenheit()}°F"


def create_all_objects():
    return {
        "person": Person("Alice", 30),
        "car": Car("Toyota", "Camry"),
        "account": BankAccount("John", 1000),
        "point": Point(3, 4),
        "dog": Dog("Rex"),
        "cat": Cat("Whiskers"),
        "circle": Circle(5),
        "bird": Bird(),
        "fish": Fish(),
        "vehicle": Vehicle("Tesla", Engine("Electric")),
        "temperature": Temperature(25)
    }