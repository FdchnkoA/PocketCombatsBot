import pyautogui
import cv2
#import pytesseract
from PIL import ImageGrab
from tkinter import *

root = Tk()

mon_height = root.winfo_screenheight()
mon_widht = root.winfo_screenwidth()

DisplaySize = [mon_height, mon_widht]

ActiveWindow_Y = mon_height / 1.78

EmulatorDisplaySize = [ActiveWindow_Y, mon_widht]

print(EmulatorDisplaySize)

base_screen = ImageGrab.grab(bbox=(0, 0, 3200, 1920))
base_screen.save('/Users/Andrew/Documents/GitHub/PocketCombatsBot/base_screen.png')
