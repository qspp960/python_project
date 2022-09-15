from turtle import Turtle

hyun = Turtle()

start = 3

for i in range(3,11):
    angle = 180 + 180 * (i-3)
    angle = 180 - (angle/i)
    for j in range(i):
        hyun.forward(100)
        hyun.right(angle)

