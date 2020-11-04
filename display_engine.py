from tkinter import *
import tkinter.ttk as ttk
from functions import *
from player_ import *
import os
from collider_ import *

class Display():
    def __init__(self, parent):
        self.parent = parent

        self.game_width = 6000
        self.game_height = 1000

        self.gamex = -2
        self.gamey = -2




        self.game_frame = Canvas(self.parent, width=self.game_width, height=self.game_height, bg="red")
        self.game_frame.place(x=self.gamex, y=self.gamey)

        self.grass = Sprite("textures/grass.png", 200)
        self.draw_bg(self.game_frame, self.game_width, self.game_height, 200, self.grass)

        self.player = Player(self, self.parent, self.game_frame)

        a = Collider(self.game_frame, 10, 80, 100, 90)
        b = Collider(self.game_frame, 50, 40, 60, 70)
        self.parent.bind('t', collider_display)

        self.test = Sprite("textures/tree1.png", 200)
        self.tree = Object_drawer(self.game_frame, self.test, 500, 210)

        self.parent.bind('<Escape>', self.show_pause_ui)

    def show_pause_ui(self, event):
        print("Showing Pause Ui")
        self.parent.bind('<Escape>', self.close_pause_ui)
        self.pause_ui = Frame(self.parent, bg="grey", width=100, height=100)
        self.pause_ui.place(x=500, y=500)

    def close_pause_ui(self, event):
        print("Closing Pause Ui")
        self.parent.bind('<Escape>', self.show_pause_ui)
        self.pause_ui.destroy()



    def print_cordinates(self):
        os.system('cls')
        print(f"GAME_FRAME:\n"
              f"-------------\n"
              f"X: {self.gamex}\n"
              f"Y: {self.gamey}\n\n"
              f"PLAYER:\n"
              f"-------------\n"
              f"X: {self.player.x}\n"
              f"Y: {self.player.y}\n"
              f"")




    def draw_bg(self, game_frame, game_frame_x, game_frame_y, image_res, image):
        print("STARTING BG CREATION")
        for i in range(round(game_frame_x / image_res)):
            for b in range(round(game_frame_y / image_res)):
                game_frame.create_image(i * image_res, b * image_res, image=image)
                print(f"BG IMAGE CREATED AT {i}, {b} | {i * image_res},  {b * image_res}")


class Object_drawer():
    def __init__(self, parent, sprite, posx, posy):
        self.sprite = sprite
        self.parent = parent

        self.object = self.parent.create_image(posx, posy, image=self.sprite)