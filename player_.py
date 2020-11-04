from tkinter import *
import tkinter.ttk as ttk
from functions import *
from collider_ import *

class Player():
    def __init__(self, display, window, parent):
        print("Player initialized")
        self.parent = parent
        self.window = window
        self.display = display
        self.x = 100
        self.y = 160
        self.stepsize = 4

        self.threashold = 100

        self.sprite = Sprite("textures/player_down.png", 60)

        self.image = parent.create_image(self.x, self.y, image=self.sprite)


        self.window.bind('<w>', self.move_up)
        self.window.bind('<s>', self.move_down)
        self.window.bind('<a>', self.move_left)
        self.window.bind('<d>', self.move_right)



    def do_every_move(self):
        #self.display.print_cordinates()
        print(self.display.gamey + self.y)


    def move_up(self, event):
        if check_collision("up", 0, 0, self.x, self.y - 30, self.stepsize):
            pass
        else:
            self.parent.move(self.image, 0, -self.stepsize)
            self.y = self.y - self.stepsize

        if  self.display.gamey + self.y < self.threashold:

            self.display.gamey = self.display.gamey + self.stepsize
            self.display.game_frame.place(x=self.display.gamex, y=self.display.gamey)


        self.do_every_move()

    def move_down(self, event):
        if check_collision("down", 0, 0, self.x, self.y + 30, self.stepsize):
            pass
        else:
            self.parent.move(self.image, 0, self.stepsize)
            self.y = self.y + self.stepsize

        if  self.display.gamey + self.y > 650 - self.threashold:

            self.display.gamey = self.display.gamey - self.stepsize
            self.display.game_frame.place(x=self.display.gamex, y=self.display.gamey)


        self.do_every_move()

    def move_left(self, event):
        self.parent.move(self.image, -self.stepsize, 0)
        self.x = self.x - self.stepsize


        self.do_every_move()

    def move_right(self, event):
        self.parent.move(self.image, self.stepsize, 0)
        self.x = self.x + self.stepsize


        self.do_every_move()