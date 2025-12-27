a = 10
b = 20
name = "John"
age = 25

print("a =", a)
print("b =", b)
print("name =", name)
print("age =", age)

num1 = "100"
num2 = 50.5

num1_int = int(num1)
num2_str = str(num2)
age_float = float(age)

print("num1 as int:", num1_int)
print("num2 as str:", num2_str)
print("age as float:", age_float)

if a < b:
    print("a is less than b")
else:
    print("a is greater or equal to b")

if age >= 18:
    print("Adult")
else:
    print("Minor")

for i in range(5):
    print("i =", i)

count = 0
while count < 3:
    print("count =", count)
    count = count + 1

def add(x, y):
    return x + y

def multiply(x, y):
    result = x * y
    return result

def greet(person):
    return "Hello, " + person

print("add(5, 3) =", add(5, 3))
print("multiply(4, 6) =", multiply(4, 6))
print("greet('Alice') =", greet("Alice"))
