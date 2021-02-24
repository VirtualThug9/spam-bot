import pyautogui as pag # importing pyautogui with the keyword "pag" so that we wouldn't need to enter such a lengthy name again and again
import time # importing the package called time

msg = "Subscribe to VirtualThug9!" # creating a variable to spam

time.sleep(5) # making the code pause for a few secs (5 secs in my case)

while True: # creating an infinte loop; this is infinite because True is always == True. So, there is no condition to set True == False
	pag.typewrite(msg) # typing where our cursor is using pyautogui
	pag.press("enter") # pressing the key "enter" using pyautogui
