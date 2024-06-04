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

    def run_clicker(self, coordinats_list):
        for x, y in coordinats_list:
            click_counter = 0
            click_until = random.randrange(5000,20000)            
            click_interval = random.randrange(52,421)/10000
            while True:
                if self.isClicking:
                    if x is not None and y is not None:
                        self.mouse.position = (x, y)
                    self.mouse.click(Button.left, 2)
                    time.sleep(click_interval)
                    click_counter += 1
                    if click_counter == click_until:
                        break

def get_coordinats():
    coordinats_list = []
    while True:
        x, y = pyautogui.position()
        print("Координаты текущего положения курсора мыши:")
        print("x =", x)
        print("y =", y)
        in_putt = input("Добавить координату/Продолжить/Завершить? (e/c/b)",)
        if in_putt.strip().lower() == "e":
            coordinats_list.append((x, y))
        elif in_putt.strip().lower() == "c":
            continue
        elif in_putt.strip().lower() == "b":
            break
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
