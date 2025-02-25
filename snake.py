from turtle import Turtle


START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIS = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            segment = Turtle('square')
            segment.color('white')
            segment.penup()  # Prevent drawing when moving
            segment.goto(pos)
            self.segments.append(segment)

    def move_forward(self):
        for seg in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DIS)

    def add_turtle(self):
        last_segment = self.segments[-1]
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()  # Prevent drawing when moving
        new_segment.goto(last_segment.xcor(), last_segment.ycor())  # Place at the last segment's position
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != 270:  # Prevent reversing
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:  # Prevent reversing
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:  # Prevent reversing
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:  # Prevent reversing
            self.head.setheading(180)