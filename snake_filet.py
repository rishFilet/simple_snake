# Snake has some position
# create a movement corresponding to the movement
# Map the keyboard input to the movement 


from pynput import keyboard
import threading
import time


flag = False


class Snake:
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.direction_x = 0
        self.direction_y = 0

    def movement(self):
        global flag
        flag = True
        for i in range(self.y, 100):
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

    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            self.current_key = key.char
        except AttributeError:
            print('special key {0} pressed'.format(
                key))
            self.current_key = key
    
    def thread(self):
        t = threading.Thread(target=self.snake.movement)
        t.start()

    def on_release(self, key):
        print(key)
        global flag
        if key == keyboard.Key.up and not flag:
            self.snake.direction_y = 1
            self.thread()
        elif key == keyboard.Key.down and not flag:
            self.snake.direction_y = -1
            self.thread()
        elif key == keyboard.Key.left:
            flag = False
            print("stopped")
            print(f"X: {self.snake.x} Y:{self.snake.y}")
        # while self.current_key == key or self.current_key == "":
        #     print(f"Still on {key}")
        # print('{0} released'.format(
        #     key))
        # if key == keyboard.Key.esc:
        #     # Stop listener
        #     return False


u_input = UserInput()
with keyboard.Listener(
        on_press=u_input.on_press,
        on_release=u_input.on_release) as listener:
    listener.join()

# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=u_input.on_press,
#     on_release=u_input.on_release)
# listener.start()



