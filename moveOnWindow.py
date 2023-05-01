import pyautogui
import cv2
#import pytesseract
from PIL import ImageGrab
from tkinter import *

root = Tk()
display_height = root.winfo_screenheight()
display_width = root.winfo_screenwidth()

DisplaySize = [display_height, display_width]
print(DisplaySize)

MemuWindow_width = display_height // 1.78

EmulatorDisplaySize = [MemuWindow_width, display_height]

print("Размеры активного окна эмулятора: " + str(EmulatorDisplaySize))

MemuWindow_CoordinateUp = display_width // 2 - MemuWindow_width // 2
MemuWindow_CoordinateDown = display_width // 2 + MemuWindow_width // 2
print(str(int(MemuWindow_CoordinateUp)) + "x" + str(0), str(int(MemuWindow_CoordinateDown)) + 'x' + str(1800))


#base_screen = ImageGrab.grab(bbox=(0, 0, 3200, 1920))
#base_screen.save('/Users/Andrew/Documents/GitHub/PocketCombatsBot/base_screen.png')
