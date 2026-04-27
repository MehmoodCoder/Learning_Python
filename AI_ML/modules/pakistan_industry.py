# modules

from iran import body
from america import tyres
from germany import chasis
from china import engine


def car_industry():
    return f"{body()},{chasis()},{engine()} and {tyres()} makes a car."

print(car_industry())

