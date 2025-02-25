import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.speed('fastest')
        self.color('blue')
        self.refresh()

    def refresh(self):
        random_y = random.randint(-300, 300)
        random_x = random.randint(-300, 300)
        self.goto(random_x, random_y)