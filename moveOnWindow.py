import pyautogui as pag
import cv2
#import pytesseract
import time
from PIL import ImageGrab
from tkinter import *
import numpy as np
import random

time.sleep(5)
root = Tk()
display_height = root.winfo_screenheight()
display_width = root.winfo_screenwidth()

DisplaySize = [display_height, display_width]
#print(DisplaySize)

MemuWindow_width = display_height // 1.78

EmulatorDisplaySize = [MemuWindow_width, display_height]

#print("Размеры активного окна эмулятора: " + str(EmulatorDisplaySize))

MemuWindow_CoordinateUp = display_width // 2 - MemuWindow_width // 2
MemuWindow_CoordinateDown = display_width // 2 + MemuWindow_width // 2
#print(str(int(MemuWindow_CoordinateUp)) + "x" + str(0), str(int(MemuWindow_CoordinateDown)) + 'x' + str(1800))

base_screen = ImageGrab.grab(bbox=(int(MemuWindow_CoordinateUp), 0, int(MemuWindow_CoordinateDown), display_height))
base_screen.save('/Users/Andrew/Documents/GitHub/PocketCombatsBot/base_screen.png')

stop = None
while stop != True:
    try:
        box = pag.locateOnScreen('StartCombatButton.png', confidence=0.8)
        StartCombatButtonPoint = pag.center(box)
        pag.click(StartCombatButtonPoint.x, StartCombatButtonPoint.y)
        stop = True
    except:
        time.sleep(3)

#try:
#    pag.moveTo(pag.locateOnScreen('StartCombatButton.png'))
#    pag.click()
#except:
#    pag.scroll(random.randint(-15, -8))
 #   pag.moveTo(pag.locateOnScreen('StartCombatButton.png'))
#    pag.click()
#    time.sleep(random.randint(1, 5))
#clean_screen.save('/Users/Andrew/Documents/GitHub/PocketCombatsBot/clean_screen.png')