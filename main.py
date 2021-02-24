import pyautogui as pag
import time

msg = "Subscribe to VirtualThug9!"

time.sleep(5)

while True:
	pag.typewrite(msg)
	pag.press("enter")