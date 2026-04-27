def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact *= i
    return fact

no = int(input("Enter a number: "))
print(f"Factorial of {no} is {factorial(no)}")