import pyautogui as pg
import keyboard
import time
import os
import pytesseract as tess
from PIL import Image #pip install pillow
from playsound import playsound
#pip install opencv-contrib-python


def start(status=True):
    status = True
    time.sleep(1)
    while status:
        if pg.locateOnScreen('new_z.png', confidence=0.5) != None:
            pg.click(88, 355)
            if pg.locateOnScreen('korets.png', confidence=0.5) == None:
                time.sleep(6)
                return pg.screenshot('screen.png')
            else:
                while True:
                    if pg.locateOnScreen('ok.png', confidence=0.5) != None:
                       pg.click(615, 502)
                    break
        else:
            print("\nGood by!")
            return pg.screenshot('screen.png')


def confirm():
    pg.click(245, 220)
    time.sleep(6)
    return pg.screenshot('screen.png')


def screen():
    return pg.screenshot('screen.png')


def ok_button():
    pg.click(615, 502)
    return

if __name__ == "__main__":
    # start()
    test()