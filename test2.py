import numpy as np
import cv2, time, pyautogui

left = 18
top = 25
right = 228
bottom = 72


while True:
    time.sleep(3)
    im = pyautogui.screenshot()
    im1 = im.crop((left, top, right, bottom))
    frame = cv2.cvtColor(np.array(im1), cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame", frame)
    time.sleep(100)
cv2.destroyAllWindows()