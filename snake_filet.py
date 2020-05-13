# Snake has some position DONE
# create a movement corresponding to the movement DONE
# Map the keyboard input to the movement


from turtle import Turtle, Screen


class Gfx:
    def __init__(self):
        super().__init__()
        self.window = Screen()
        self.window.bgcolor('black')

    def start(self):
        self.window.mainloop()


# Here we define the snake character/object and give it initial values for the position. direction_x and _y are used to determine which direction. +1 is up or right and -1 is down or left
class Snake(Gfx):
    def __init__(self):
        super().__init__()
        self.head = Turtle()
        self.head.color('green')
        self.head.penup()
        self.snake_speed = 5
        self.keyboard_preses()
        self.window.listen()
        self.movement()

    # flag is a global variable used to determine when the loop should be stopped when a certain key is presed
    def movement(self):
        self.head.forward(self.snake_speed)
        self.window.ontimer(self.movement, 10)

    def keyboard_preses(self):
        self.window.onkey(lambda: self.head.setheading(90), 'Up')
        self.window.onkey(lambda: self.head.setheading(180), 'Left')
        self.window.onkey(lambda: self.head.setheading(0), 'Right')
        self.window.onkey(lambda: self.head.setheading(270), 'Down')


Snake().start()
