import turtle
import math

# Screen Setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Heart Animation")
screen.setup(width=800, height=800)

# Turtle Setup
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Heart Mathematical Equation
def heart_a(k):
    return 15 * math.sin(k)**3

def heart_b(k):
    return 12 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)

# Drawing Outer Glowing Lines
for i in range(1600):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    
    # Dynamic Color Transition (Red to Pink gradient)
    red_val = 1.0
    green_val = abs(math.sin(i / 100)) * 0.3
    blue_val = abs(math.cos(i / 100)) * 0.5
    pen.color((red_val, green_val, blue_val))
    
    # Calculate Points
    x = heart_a(i) * 20
    y = heart_b(i) * 20
    pen.goto(x, y)

turtle.done()