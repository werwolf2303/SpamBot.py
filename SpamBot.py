import pyautogui
import threading
import time
import sys
import keyboard
t = "true"

def create(tospam):
    def loop1_10():
        while(t):
            if (keyboard.is_pressed("esc")):
                break
            pyautogui.typewrite(tospam)
            pyautogui.press("enter")
    thread = threading.Thread(target=loop1_10())
    thread.start()

def main(argv):
    print("You can spam also insults from a list type arg -insult")
    print("Press ESC to stop spamming")
    arg = argv[1].split(" ")
    create(argv[1])
    time.sleep(5)
if __name__ == '__main__':
    main(sys.argv)


