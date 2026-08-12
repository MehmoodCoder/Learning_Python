def my_function():
    print("Hello from a function")

my_function()

# Simple Arguments and parameters

def adder(x,y):
    return x + y

a,b = 10,90
print(f"Sum of {a} and {b} is {adder(a,b)}.")

# Positional Arguments and Parameters
# Default parameters

def bill_gen(name="Hamza",bill=450): # but whenever it gives value it change its default values.
    return f"Hi {name}, you paid {bill}, Thank you."

name,bill = "Ali",123
print(bill_gen(name,bill)) # bill_gen(name,bill) is wrong because of positional arguments and parameters.

# solution : 
# Keyword Argument

print(bill_gen(name =  "Ahmad", bill = 124)) 












