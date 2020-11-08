import turtle
import random

fred = turtle.Pen()
fred.shape("turtle")
colors= ["red", "green", "blue", "orange",  "yellow"]

def square(size, position, color):
    fred.up()
    fred.goto(position[0], position[1])
    fred.color(color)
    fred.down()
    for i in range(4):
        fred.forward(size)
        fred.left(90)

for i in range(10):
	s = random.randrange(10,201)
	x = random.randrange(-200, 201)
	y = random.randrange(-200,200)
	l = [x, y]
	c = random.choice(colors)
	square(s, l, c)


