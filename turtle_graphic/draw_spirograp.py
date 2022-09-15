import turtle as t
import random

hyun = t.Turtle()
t.colormode(255)
hyun.speed('fastest')


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color_t = (r,g,b)
    return color_t


for i in range(100):
    hyun.color(random_color())
    hyun.circle(100)
    hyun.left(5)

def draw_spirograp(size_of_gap):
    for i in range(int(360/size_of_gap)):
        hyun.color(random_color())
        hyun.circle(100)
        hyun.setheading(hyun.heading()+size_of_gap)


draw_spirograp(5)
