from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snakes_body = []
        self.create_snake()
        self.head = self.snakes_body[0]

    def create_snake(self):
        for start_position in STARTING_POSITION:
            self.add_snake_body(start_position)

    def add_snake_body(self, position):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.snakes_body.append(new_snake)

    def extend(self):
        self.add_snake_body(self.snakes_body[-1].position())

    def move(self):
        for snake_num in range(len(self.snakes_body) - 1, 0, -1):
            new_x = self.snakes_body[snake_num - 1].xcor()
            new_y = self.snakes_body[snake_num - 1].ycor()
            self.snakes_body[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


