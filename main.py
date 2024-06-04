from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
import pyautogui
import time
import random

class CLICKERR():
    def __init__(self) -> None:
        self.isClicking = False
        self.hotkey = Key.shift
        self.mouse = Controller()

    def toggle_clicker(self):
        self.isClicking = not self.isClicking
        if self.isClicking:
            print("Clicker is enabled")            
        else:
            print("Clicker is disabled")

    def on_key_press(self, key):
        if key == self.hotkey:
            self.toggle_clicker()

    def generate_click_params(self):
        return random.randrange(100, 500), random.randrange(52, 421) / 10000

    def run_clicker(self, coordinates_list):
        while True:
            for x, y in coordinates_list:
                x += random.randint(-7, 7)
                y += random.randint(-7, 7)
                click_counter = 0
                click_until, click_interval = self.generate_click_params()
                while click_counter < click_until and self.isClicking:
                    if x is not None and y is not None:
                        self.mouse.position = (x, y)
                    self.mouse.click(Button.left, 2)
                    time.sleep(click_interval)
                    click_counter += 1
                    if not self.isClicking:  # Добавлено условие для остановки кликера
                        break

def get_coordinats():
    coordinats_list = []
    while True:
        in_putt = input("Добавить координаты/Завершить сбор координат? (enter/n)",)
        x, y = pyautogui.position()
        print("Координаты текущего положения курсора мыши:")
        print("x =", x)
        print("y =", y)
        if in_putt.strip().lower() == "n":
            break 
        coordinats_list.append((x, y))
    return coordinats_list

def main():
    cl = CLICKERR()
    coordinats_list = get_coordinats()
    print(coordinats_list)
    print('Please press shift to start clicking and the same key to stop!')    
    listener = Listener(on_press=cl.on_key_press)
    listener.start()
    cl.run_clicker(coordinats_list)
    listener.join()

if __name__ == "__main__":
    main()
