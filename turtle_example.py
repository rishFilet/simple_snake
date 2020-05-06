from turtle import Turtle, Screen

wn = Screen()
wn.bgcolor('lightblue')

spaceship = Turtle()
spaceship.color('red')

#Removes the pen line from the drawing
spaceship.penup()

speed = 1


def travel():
    spaceship.forward(speed)
    # This will call the function so that the turtle moves forward in the specified direction every X milliseconds
    wn.ontimer(travel, 10)

#setheaing sets the direction the turtle moves. 
wn.onkey(lambda: spaceship.setheading(90), 'Up')
wn.onkey(lambda: spaceship.setheading(180), 'Left')
wn.onkey(lambda: spaceship.setheading(0), 'Right')
wn.onkey(lambda: spaceship.setheading(270), 'Down')

wn.listen()

travel()

wn.mainloop()
