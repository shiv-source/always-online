import pyautogui
import random
import time


pyautogui.FAILSAFE = False

print('press Ctrl+c to quit')

try:
    while True:
        pyautogui.press('shift')
        sleep_time = random.randint(30, 90)
        time.sleep(sleep_time)
except KeyboardInterrupt:
    print('/n')
