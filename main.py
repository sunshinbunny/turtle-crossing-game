import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

n=0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car.car_move()
    screen.update()
    n+=1

    if n%6 == 0:
        car.create_car()

    for cars in car.all_cars:
        if player.distance(cars) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.reset_position()
        car.increase_speed()
        scoreboard.level_increase()



screen.exitonclick()