# from pynput.keyboard import Key, Listener
# from pynput.mouse import Button, Controller
# import time

# cleck_interval = 0.1

# class CLICKERR():
#     def __init__(self) -> None:
#         self.isClicking = False
#         self.hotkey = Key.shift
#         self.mouse = Controller()

#     def toggle_clicker(self):
#         self.isClicking = not self.isClicking
#         if self.isClicking:
#             print("Кликер включен")            
#         else:
#             print("Кликер отключен")

#     def on_key_press(self, key):
#         if key == self.hotkey:
#             self.toggle_clicker()

#     def run_clicker(self):
#         while True:
#             if self.isClicking:
#                 self.mouse.click(Button.left, 2)
#                 time.sleep(cleck_interval)

# def main():
#     cl = CLICKERR()
#     print('Please tab f1 for start clicking and the same key for stoping!')
#     listener = Listener(on_press=cl.on_key_press)
#     listener.start()
#     cl.run_clicker()
#     listener.join()

# if __name__=="__main__":
#     main()