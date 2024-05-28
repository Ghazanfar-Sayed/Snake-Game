from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.color('blue')
        self.speed("fastest")
        self.penup()
        self.refresh()
    
    def refresh(self):
        random_x = random.randint(-265, 265)
        random_y = random.randint(-265, 265)

        self.goto((random_x, random_y))
