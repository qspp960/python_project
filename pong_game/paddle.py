from turtle import Turtle



class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.goto(position[0], position[1])
        self.shape("square")
        self.shapesize(stretch_wid=5.0,stretch_len=1.0)
        self.color("white")

    def go_up(self):
        new_y = self.ycor() + 20
        self.penup()
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.penup()
        self.goto(self.xcor(),new_y)



