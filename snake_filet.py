# Snake has some position
# create a movement corresponding to the movement
# Map the keyboard input to the movement 


from pynput import keyboard
import threading
import time
import turtle


flag = False

screen = turtle.getscreen()
screen.title("Snake Game")
screen.bgcolor("white")
screen.setup(width=500, height=500)

head = turtle.Turtle()
head.shape("square")
head.color("green")


# Here we define the snake character/object and give it initial values for the position. direction_x and _y are used to determine which direction. +1 is up or right and -1 is down or left
class Snake:
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.direction_x = 0
        self.direction_y = 0

    #flag is a global variable used to determine when the loop should be stopped when a certain key is presed 
    def movement(self):
        global flag
        flag = True
        #these if else statements start the loop from the last position the snake was in
        if self.direction_x != 0:
            start = self.x
        elif self.direction_y != 0:
            start = self.y
        else:
            start = 0
        for i in range(start, 100):
            if not flag:
                break
            self.x = self.x + self.direction_x
            self.y = self.y + self.direction_y
            print(f"X: {self.x} Y:{self.y}")
            time.sleep(1)


class UserInput:
    def __init__(self):
        super().__init__()
        self.snake = Snake()
        self.last_key_press = ""

    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed, not operational for game'.format(
                key.char))
        except AttributeError:
            pass
            # print('special key {0} pressed'.format(
            #     key))
    
    #Threading is when the computer creates multiple processes in parallel. Here threading is necessary to continue the loop while also listening for key presses
    def thread(self):
        t = threading.Thread(target=self.snake.movement)
        t.start()

# move_in_direction determines which way the snake should move and checks if the last key presses were the same as before or in the opposite direction. Snake needs to turn 90 degrees and not 180 degrees
    def move_in_direction(self, key_press, opposite_direction, dir_x, dir_y):
        global flag
        if self.last_key_press != key_press and self.last_key_press != opposite_direction:
            self.snake.direction_y = dir_y
            self.snake.direction_x = dir_x
            self.thread()
        else:
            if self.last_key_press == key_press:
                print("Already moving in that direction, can't go faster")
            elif self.last_key_press == opposite_direction:
                print("Cannot move in the opposite direction, turn first")
            flag = True

    def on_release(self, key):
        global flag
        flag = False
        if key == keyboard.Key.up and not flag:
            self.move_in_direction(key, keyboard.Key.down, 0, 1)
        elif key == keyboard.Key.down and not flag:
            self.move_in_direction(key, keyboard.Key.up, 0, -1)
        elif key == keyboard.Key.left and not flag:
            self.move_in_direction(key, keyboard.Key.right, -1, 0)
        elif key == keyboard.Key.right and not flag:
            self.move_in_direction(key, keyboard.Key.left, 1, 0)
        elif key == keyboard.Key.esc:
            print("stopped")
            print("Game Over")
        self.last_key_press = key


u_input = UserInput()
with keyboard.Listener(
        on_press=u_input.on_press,
        on_release=u_input.on_release) as listener:
    listener.join()




