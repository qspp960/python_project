from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font = FONT)


    def reset(self):
        if self.score > self.high_score:
            with open('data.txt','w') as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
    #def game_over(self):
    #    self.goto(0,0)
    #    self.write("GAME OVER",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()



