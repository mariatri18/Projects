import turtle
import random

fred = turtle.Pen()
fred.shape("turtle")


def square(size):
    for i in range(4):
        fred.forward(size)
        fred.left(90)
for i in range(10):
    x = random.randrange(-200,201)
    y = random.randrange(-200,201)
    print(x,y)       
    fred.up()
    fred.goto(x,y)
    fred.down()
    z = random.randrange(10,201)
    square(z)
