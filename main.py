import pyautogui, time, pydirectinput, cv2, threading, keyboard
import numpy as np
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener


def keyCheck():
    with Listener(on_press=pressed, on_release=released) as detector:
        detector.join()

def pressed(key):
    print('Pressed: ', key)


def released(key):
    global loopControl
    print('Released: ', key)
    if key == Key.f11:
        loopControl = not loopControl
    if key == Key.f12:
        return False

def hpmpDetect():
    global loopControl
    left = 27
    top = 33
    right = 192
    bottom = 35
    while True:
        while loopControl:
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

            if round((nonZeroCountRed*100)/191) <= 70:
                pressButton('4')
                time.sleep(0.1)
                pressButton('6')
                time.sleep(0.1)
            if round((nonZeroCountBlue*100)/191) <= 30:
                pressButton('3')
                time.sleep(0.1)

def pressButton(button):
    pydirectinput.keyDown(button)
    time.sleep(0.5)
    pydirectinput.keyUp(button)

def attackStart():
    global loopControl
    while True:
        while loopControl:
            loopSequence = ['z', 'r', '1', '2','z','r','2']
            for key in loopSequence:
                pressButton(key)
                time.sleep(0.1)
            time.sleep(0.1)

# Press the green button in the gutter to run the script.4z6r32
if __name__ == '__main__':
    loopControl = False
    print('Started')
    time.sleep(3)

    #t1 = threading.Thread(target=keyCheck, daemon=True)
    #t1.start()

    t2 = threading.Thread(target=hpmpDetect, daemon=True)
    t2.start()

    t3 = threading.Thread(target=attackStart, daemon=True)
    t3.start()

    print('Koxp is running')
    while True:

        def on_scroll(x, y, dx, dy):
            global loopControl
            print(x, y, dx, dy)
            loopControl = not loopControl
            time.sleep(1)


        with Listener(on_scroll=on_scroll) as listener:
            listener.join()

# See PyCharm help at https://www.jetbrains.com/r12help/pycharm/
