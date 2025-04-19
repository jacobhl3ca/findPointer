import pyautogui # https://pyautogui.readthedocs.io/en/latest/quickstart.html
pyautogui.FAILSAFE = True
import time
import logging
import os

time.sleep(2)  # Reduced delay for faster execution
position = pyautogui.position()
print(f"The position is: {position}")

print(pyautogui.size())