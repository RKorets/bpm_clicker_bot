import pyautogui as pg
import keyboard
import time
import os
import pytesseract as tess
from PIL import Image #pip install pillow
from playsound import playsound
#pip install opencv-contrib-python


def start():
    status = True
    time.sleep(2)
    while status:
        if pg.locateOnScreen('new_z.png', grayscale=True, confidence=0.5) is not None:
            print("point new")
            if pg.locateOnScreen('korets.png', grayscale=True, confidence=0.5) is None:
                time.sleep(1)
                playsound('mario.mp3')
                keyboard.wait("shift")
            else:
                while True:
                    if pg.locateOnScreen('ok.png', grayscale=True, confidence=0.5) is not None:
                        pg.click(615, 502) # ок - немає заявок для обробки
                        pg.click(121, 437) # наступна заявка
                        time.sleep(0.1)
                        pg.click(121, 437)  # наступна заявка
                        print("point next order")
                        #break
                    if pg.locateOnScreen('korets.png', grayscale=True, confidence=0.5) is None:
                        time.sleep(1)
                        playsound('mario.mp3')
                        keyboard.wait("shift")
                    print("point ok")
                    #break
        else:
            print("\nGood by!")
            break


#запускати з дерикторії папки
#sudo python3 clicker.py

if __name__ == "__main__":
    start()
