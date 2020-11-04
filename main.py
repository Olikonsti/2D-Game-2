from tkinter import *
import tkinter.ttk as ttk
from functions import *

from display_engine import *

TITLE = "TEST_2D_GAME_2"
VERSION = 1.0


wd = Tk()
wd.geometry("1000x650")
wd.iconbitmap("textures/Logo.ico")
wd.title(f"{TITLE} | V: {str(VERSION)}")

display = Display(wd)

wd.mainloop()


