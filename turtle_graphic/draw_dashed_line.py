from turtle import Turtle

hyun = Turtle()
hyun.shape("arrow")

for i in range(10):
    hyun.forward(30)
    hyun.penup()
    hyun.forward(30)
    hyun.pendown()