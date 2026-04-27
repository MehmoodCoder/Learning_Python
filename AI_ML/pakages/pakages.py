# pakages
# 1.

# from east.iran import body
# from west.america import tyres
# from west.germany import chasis
# from east.china import engine


# def car_industry():
#     return f"{body()},{chasis()},{engine()} and {tyres()} makes a car."

# print(car_industry())

# 2.

from west import america,germany
from east import china,iran

def car_industry():
    return f"{germany.body()},{china.chasis()},{iran.engine()} and {america.tyres()} makes a car."

print(car_industry())
