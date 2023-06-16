from turtle import Turtle
_STARTING_POSITIONS = [(-20,0), (0, 0), (20, 0)]
_MOVE_DIST = 20
_UP = 90
_DOWN = -90
_LEFT = 180
_RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        for position in _STARTING_POSITIONS:
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(position)
            self.snake_body.append(new_square)

    def move(self):
        for part_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part_num - 1].xcor()
            new_y = self.snake_body[part_num - 1].ycor()

            self.snake_body[part_num].goto(new_x, new_y)

        self.snake_head.forward(_MOVE_DIST)

    def up(self):
        if self.snake_head.heading() != _DOWN:
            self.snake_head.setheading(_UP)
    def down(self):
        if self.snake_head.heading() != _UP:
            self.snake_head.setheading(_DOWN)
    def left(self):
        if self.snake_head.heading() != _RIGHT:
            self.snake_head.setheading(_LEFT)
    def right(self):
        if self.snake_head.heading() != _LEFT:
            self.snake_head.setheading(_RIGHT)
