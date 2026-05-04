# def factorial(no):
#     fact = 1
#     for i in range(1,no+1):
#         fact *= i
#     return fact

# for no in range(1,11):
#     print(f"Factorial of {no} is {factorial(no)}")


# Recursive Functions


def recursive_func(no):
    if no <= 1:
        return 1
    else:
        a = no * recursive_func(no-1)
        return a

for i in range(1,11):
    print(f"Factorial of {i} is {recursive_func(i)}")


