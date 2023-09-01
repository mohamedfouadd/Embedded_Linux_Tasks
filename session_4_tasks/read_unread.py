import pyautogui
import time

pyautogui.press('win')
time.sleep(2)
pyautogui.write('firefox')
time.sleep(2)
pyautogui.press('enter')
time.sleep(5)
pyautogui.hotkey('ctrl','n')
time.sleep(2)
pyautogui.write('https://mail.google.com/mail/')
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)

image_path = '~/Pictures/Screenshots/Screenshot from 2023-09-01 14-12-41.png'
image_location = pyautogui.locateOnScreen(image_path)
time.sleep(1)
image_center = pyautogui.center(image_location)
time.sleep(1)
pyautogui.click(image_center)
time.sleep(3)

image_path = '~/Pictures/Screenshots/Screenshot from 2023-09-01 14-12-52.png'
image_location = pyautogui.locateOnScreen(image_path)
time.sleep(1)
image_center = pyautogui.center(image_location)
time.sleep(1)
pyautogui.click(image_center)
time.sleep(3)