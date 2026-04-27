def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {subtract(a, b)}")
print(f"{a} * {b} = {multiply(a, b)}")
try:
    print(f"{a} / {b} = {divide(a, b)}")
except ValueError as e:
    print(e)