from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.write(f"LEVEL: {self.level}",align='left',font=FONT)

    def win_refresh(self):
        self.level += 1
        self.clear()
        self.write(f"LEVEL: {self.level}", align='left', font=FONT)

    def lose_refresh(self):
        self.level = 1
        self.clear()
        self.write(f"LEVEL: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align='center',font=FONT)

