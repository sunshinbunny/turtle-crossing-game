from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



#Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
# and move to the left edge of the screen.

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5

    def create_car(self):
        new_car = Turtle()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(300, random.randint(-250, 250))
        self.all_cars.append(new_car)

    def car_move(self):
        for new_car in self.all_cars:
            new_car.forward(self.STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT





