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
#     def on_press(self, key):
#         try:
#             print('alphanumeric key {0} pressed, not operational for game'.format(
#                 key.char))
#         except AttributeError:
#             pass
#             # print('special key {0} pressed'.format(
#             #     key))

#     #Threading is when the computer creates multiple processes in parallel. Here threading is necessary to continue the loop while also listening for key presses
#     def thread(self):
#         t = threading.Thread(target=self.snake.movement)
#         t.start()

# # move_in_direction determines which way the snake should move and checks if the last key presses were the same as before or in the opposite direction. Snake needs to turn 90 degrees and not 180 degrees
#     def move_in_direction(self, key_press, opposite_direction, dir_x, dir_y):
#         global flag
#         if self.last_key_press != key_press and self.last_key_press != opposite_direction:
#             self.snake.direction_y = dir_y
#             self.snake.direction_x = dir_x
#             self.thread()
#         else:
#             if self.last_key_press == key_press:
#                 print("Already moving in that direction, can't go faster")
#             elif self.last_key_press == opposite_direction:
#                 print("Cannot move in the opposite direction, turn first")
#             flag = True

#     def on_release(self, key):
#         global flag
#         flag = False
#         if key == keyboard.Key.up and not flag:
#             self.move_in_direction(key, keyboard.Key.down, 0, 1)
#         elif key == keyboard.Key.down and not flag:
#             self.move_in_direction(key, keyboard.Key.up, 0, -1)
#         elif key == keyboard.Key.left and not flag:
#             self.move_in_direction(key, keyboard.Key.right, -1, 0)
#         elif key == keyboard.Key.right and not flag:
#             self.move_in_direction(key, keyboard.Key.left, 1, 0)
#         elif key == keyboard.Key.esc:
#             print("stopped")
#             print("Game Over")
#         self.last_key_press = key


# u_input = UserInput()
# with keyboard.Listener(
#         on_press=u_input.on_press,
#         on_release=u_input.on_release) as listener:
#     listener.join()
