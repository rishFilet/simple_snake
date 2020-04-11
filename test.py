from pynput import keyboard
import threading
import time

clicks_running = False


class Snake:
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0

    def start_clicks(self, x=0, y=0):
        global clicks_running
        clicks_running = True

        # Clicks 50 times at location (400, 400) with left mouse button every 1 second
        for x in range(50):
            if not clicks_running:
                break
            else:
                self.x = self.x + x
                self.y = self.y + y
                print(f"X: {self.x} Y:{self.y}")
                time.sleep(1)


class UserInput:
    def __init__(self):
        super().__init__()
        self.snake = Snake()

    def on_press(self, key):
        global clicks_running
        print(key)
        if key == keyboard.Key.up and not clicks_running:
            t = threading.Thread(target=self.snake.start_clicks(y=1))
            t.start()
        elif key == keyboard.Key.down:
            # I WANT TO STOP FOR LOOP WHEN I PRESS F12
            clicks_running = False
            print(f"X: {self.snake.x} Y:{self.snake.y}")


ua = UserInput()
# Listens for keyboard inputs
with keyboard.Listener(on_press=ua.on_press) as listener:
    listener.join()
