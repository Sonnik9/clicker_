# # import keyboard
# # import mouse
# # import time

# # isClicking = False

# # def set_clicker():
# #     global isClicking
# #     if isClicking:
# #         isClicking = False
# #         print('Off')
# #     else:
# #         isClicking = True
# #         print('On')

# # keyboard.add_hotkey('Alt + z', set_clicker)

# # while True:
# #     if isClicking:
# #         mouse.double_click(button = 'left')
# #         time.sleep(0.6)


#     # def run_clicker(self, coordinats_list):
#     #     while True:
#     #         for x, y in coordinats_list:
#     #             x, y =  x +  random.randint(-7, 7), y +  random.randint(-7, 7)
#     #             click_counter = 0
#     #             click_until = random.randrange(100, 500) 
#     #             click_interval = random.randrange(52,421)/10000
#     #             while True:         
#     #                 if self.isClicking:
#     #                     if x is not None and y is not None:
#     #                         self.mouse.position = (x, y)
#     #                     self.mouse.click(Button.left, 2)
#     #                     time.sleep(click_interval)
#     #                     click_counter += 1
#     #                     if click_counter == click_until:
#     #                         break


# import tkinter as tk
# from pynput.keyboard import Key, Listener
# from pynput.mouse import Button, Controller
# import pyautogui
# import time
# import random
# import threading

# class CLICKERR():
#     def __init__(self) -> None:
#         self.isClicking = False
#         self.hotkey = Key.shift
#         self.mouse = Controller()
#         self.listener = Listener(on_press=self.on_key_press)

#     def toggle_clicker(self):
#         self.isClicking = not self.isClicking
#         if self.isClicking:
#             print("Clicker is enabled")            
#         else:
#             print("Clicker is disabled")

#     def on_key_press(self, key):
#         if key == self.hotkey:
#             self.toggle_clicker()

#     def generate_click_params(self):
#         return random.randrange(100, 500), random.randrange(52, 421) / 10000

#     def run_clicker(self, coordinates_list):
#         while True:
#             for x, y in coordinates_list:
#                 x += random.randint(-7, 7)
#                 y += random.randint(-7, 7)
#                 click_counter = 0
#                 click_until, click_interval = self.generate_click_params()
#                 while click_counter < click_until and self.isClicking:
#                     if x is not None and y is not None:
#                         self.mouse.position = (x, y)
#                     self.mouse.click(Button.left, 2)
#                     time.sleep(click_interval)
#                     click_counter += 1
#                     if not self.isClicking:
#                         break

#     def start_listener(self):
#         self.listener.start()

#     def stop_listener(self):
#         self.listener.stop()

# def get_coordinats():
#     coordinats_list = []
#     while True:
#         in_putt = input("Добавить координаты/Завершить сбор координат? (enter/n)",)
#         x, y = pyautogui.position()
#         print("Координаты текущего положения курсора мыши:")
#         print("x =", x)
#         print("y =", y)
#         if in_putt.strip().lower() == "n":
#             break 
#         coordinats_list.append((x, y))
#     return coordinats_list

# def main():
#     cl = CLICKERR()

#     def start_clicker():
#         coordinats_list = get_coordinats()
#         cl.start_listener()
#         threading.Thread(target=cl.run_clicker, args=(coordinats_list,)).start()

#     def stop_clicker():
#         cl.stop_listener()

#     root = tk.Tk()
#     root.title("Clicker Interface")

#     start_button = tk.Button(root, text="Start Clicker", command=start_clicker)
#     start_button.pack(pady=10)

#     stop_button = tk.Button(root, text="Stop Clicker", command=stop_clicker)
#     stop_button.pack(pady=10)

#     root.mainloop()

# if __name__ == "__main__":
#     main()

# #  python test.py

# import tkinter as tk
# from pynput.keyboard import Key, Listener
# from pynput.mouse import Button, Controller
# import pyautogui
# import time
# import random
# import threading

# class CLICKERR():
#     def __init__(self) -> None:
#         self.isClicking = False
#         self.hotkey = Key.shift
#         self.mouse = Controller()
#         self.listener = Listener(on_press=self.on_key_press)

#     def toggle_clicker(self):
#         self.isClicking = not self.isClicking
#         if self.isClicking:
#             print("Clicker is enabled")            
#         else:
#             print("Clicker is disabled")

#     def on_key_press(self, key):
#         if key == self.hotkey:
#             self.toggle_clicker()

#     def generate_click_params(self):
#         return random.randrange(100, 500), random.randrange(52, 421) / 10000

#     def run_clicker(self, coordinates_list):
#         while True:
#             for x, y in coordinates_list:
#                 x += random.randint(-7, 7)
#                 y += random.randint(-7, 7)
#                 click_counter = 0
#                 click_until, click_interval = self.generate_click_params()
#                 while click_counter < click_until and self.isClicking:
#                     if x is not None and y is not None:
#                         self.mouse.position = (x, y)
#                     self.mouse.click(Button.left, 2)
#                     time.sleep(click_interval)
#                     click_counter += 1
#                     if not self.isClicking:
#                         break

#     def start_listener(self):
#         self.listener.start()

#     def stop_listener(self):
#         self.listener.stop()

# def get_coordinats():
#     coordinats_list = []
#     while True:
#         in_putt = input("Добавить координаты/Завершить сбор координат? (enter/n)",)
#         x, y = pyautogui.position()
#         print("Координаты текущего положения курсора мыши:")
#         print("x =", x)
#         print("y =", y)
#         if in_putt.strip().lower() == "n":
#             break 
#         coordinats_list.append((x, y))
#     return coordinats_list

# def main():
#     cl = CLICKERR()

#     def start_clicker():
#         coordinats_list = get_coordinats()
#         cl.start_listener()
#         threading.Thread(target=cl.run_clicker, args=(coordinats_list,)).start()

#     def stop_clicker():
#         cl.stop_listener()

#     def on_drag(event):
#         root.geometry(f"+{event.x_root}+{event.y_root}")

#     root = tk.Tk()
#     root.title("Clicker Interface")

#     start_button = tk.Button(root, text="Start Clicker", command=start_clicker)
#     start_button.pack(pady=10)

#     stop_button = tk.Button(root, text="Stop Clicker", command=stop_clicker)
#     stop_button.pack(pady=10)

#     # Привязка функции on_drag к событию перемещения мыши
#     root.bind('<B1-Motion>', on_drag)

#     root.mainloop()

# if __name__ == "__main__":
#     main()



# import tkinter as tk
# import subprocess
# from pynput.keyboard import Key, Listener
# from pynput.mouse import Button, Controller
# import pyautogui
# import time
# import random
# import threading

# class CLICKERR():
#     def __init__(self) -> None:
#         self.isClicking = False
#         self.hotkey = Key.shift
#         self.mouse = Controller()
#         self.listener = Listener(on_press=self.on_key_press)

#     def toggle_clicker(self):
#         self.isClicking = not self.isClicking
#         if self.isClicking:
#             print("Clicker is enabled")            
#         else:
#             print("Clicker is disabled")

#     def on_key_press(self, key):
#         if key == self.hotkey:
#             self.toggle_clicker()

#     def generate_click_params(self):
#         return random.randrange(100, 500), random.randrange(52, 421) / 10000

#     def run_clicker(self, coordinates_list):
#         while True:
#             for x, y in coordinates_list:
#                 x += random.randint(-7, 7)
#                 y += random.randint(-7, 7)
#                 click_counter = 0
#                 click_until, click_interval = self.generate_click_params()
#                 while click_counter < click_until and self.isClicking:
#                     if x is not None and y is not None:
#                         self.mouse.position = (x, y)
#                     self.mouse.click(Button.left, 2)
#                     time.sleep(click_interval)
#                     click_counter += 1
#                     if not self.isClicking:
#                         break

#     def start_listener(self):
#         self.listener.start()

#     def stop_listener(self):
#         self.listener.stop()

# def get_coordinats():
#     coordinats_list = []
#     while True:
#         in_putt = input("Добавить координаты/Завершить сбор координат? (enter/n)",)
#         x, y = pyautogui.position()
#         print("Координаты текущего положения курсора мыши:")
#         print("x =", x)
#         print("y =", y)
#         if in_putt.strip().lower() == "n":
#             break 
#         coordinats_list.append((x, y))
#     return coordinats_list

# def main():
#     cl = CLICKERR()

#     def start_clicker():
#         coordinats_list = get_coordinats()
#         cl.start_listener()
#         threading.Thread(target=cl.run_clicker, args=(coordinats_list,)).start()

#     def stop_clicker():
#         cl.stop_listener()

#     def on_drag(event):
#         root.geometry(f"+{event.x_root}+{event.y_root}")

#     def open_terminal():
#         subprocess.Popen('cmd.exe')

#     root = tk.Tk()
#     root.title("Clicker Interface")

#     start_button = tk.Button(root, text="Start Clicker", command=start_clicker)
#     start_button.pack(pady=10)

#     stop_button = tk.Button(root, text="Stop Clicker", command=stop_clicker)
#     stop_button.pack(pady=10)

#     open_terminal_button = tk.Button(root, text="Open Terminal", command=open_terminal)
#     open_terminal_button.pack(pady=10)

#     # Привязка функции on_drag к событию перемещения мыши
#     root.bind('<B1-Motion>', on_drag)

#     root.mainloop()

# if __name__ == "__main__":
#     main()

