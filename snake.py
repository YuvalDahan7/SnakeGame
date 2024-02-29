from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

# I have to rescue the values of the things that I would like to change, so if there is any problem with the code,
# it will be more easily to figured it out.


class Snake:
    # Constructor
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.shapesize(0.5)
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # add a new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg_num - 1].xcor()
            y_position = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_position, y_position)
        self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
