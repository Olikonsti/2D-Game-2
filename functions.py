from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk

def Sprite(picture, res):
    im = Image.open(picture).convert("RGBA").resize((res, res), Image.BOX)
    pic = ImageTk.PhotoImage(im)
    cor = Image.open(picture)
    print(cor.mode)
    return pic