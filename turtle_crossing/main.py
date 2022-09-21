import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.move,'w')
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    if car_manager.crush(player):
        player.refresh()
        game_is_on = False
        scoreboard.game_over()

    if player.ycor() > 280:
        player.refresh()
        scoreboard.win_refresh()
        car_manager.level_up()


screen.exitonclick()
