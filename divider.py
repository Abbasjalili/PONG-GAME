from turtle import Turtle

START_POS = [(0, 20), (0, -20), (0, 80), (0, -80), (0, 140), (0, -140), (0, 200), (0, -200), (0, 260), (0, -260)]

class Divider(Turtle):

    def __init__(self):
        self.wall = []
        self.create_wall()
        


    def create_wall(self):
        for position in START_POS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle(shape = "square")
        t.penup()
        t.color("white")
        t.goto(position)
        t.shapesize(2, 0.1)
        self.wall.append(t)
