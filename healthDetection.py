import cv2, pyautogui, time
import numpy as np

def hpmpDetect():
    left = 27
    top = 33
    right = 192
    bottom = 35
    im = pyautogui.screenshot(region=(left,top,right,bottom))
    im.save("HPbar2.png")

    img1 = cv2.imread("HPbar2.png")
    hsv = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)

    #upper red
    lower_red2 = np.array([170,50,50])
    upper_red2 = np.array([180,255,255])

    # upper blue
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    for array in mask2:
        nonZeroCountRed = np.count_nonzero(array)
        if nonZeroCountRed:
            print(nonZeroCountRed)
            break
    print(f'Char has %{round((nonZeroCountRed*100)/191)} HP!')

    for array2 in mask1:
        nonZeroCountBlue = np.count_nonzero(array2)
        if nonZeroCountBlue:
            print(nonZeroCountBlue)
            break
    print(f'Char has %{round((nonZeroCountBlue*100)/191)} MP!')

    return round((nonZeroCountRed*100)/191), round((nonZeroCountBlue*100)/191)

print('Starting in 3 seconds!')
time.sleep(3)
hpBar, mpBar = hpmpDetect()
print(hpBar)
print(mpBar)