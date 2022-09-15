import turtle as t
import random

hyun = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_t = (r,g,b)
    return color_t


directions = [0,90,180,270]
hyun.pensize(10)

for i in range(20):
    hyun.color(random_color())
    hyun.forward(30)
    hyun.setheading(random.choice(directions))




