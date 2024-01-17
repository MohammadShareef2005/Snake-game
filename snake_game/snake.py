from turtle import Turtle

axis = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
Down = 270
Right = 0
Left = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for n in axis:
            self.add_e(n)

    def add_e(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend_b(self):
        self.add_e(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_num - 1].xcor()
            y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x, y)
        self.segments[0].forward(move_distance)

    def up(self):
        if self.segments[0].heading() != Down:
            self.segments[0].setheading(UP)

    def left(self):
        if self.segments[0].heading() != Right:
            self.segments[0].setheading(Left)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(Down)

    def right(self):
        if self.segments[0].heading() != Left:
            self.segments[0].setheading(Right)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
