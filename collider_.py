from tkinter import *

collider_list = []

def get_collider_list():
    return collider_list

def collider_display(event=None):
    print("ENTERED COLLIDER DEBUG MODE")
    for i in collider_list:
        i.frame = Frame(i.parent, bg="red", height=i.height, width=i.width)
        i.frame.place(x=i.x, y=i.y)


def check_collision(direction, x, y, xdown=None, ydown=None, step_size=0):
    collision = False
    if direction == "up":
        for i in collider_list:
            if ydown - 2 <= i.ydown and xdown - step_size <= i.xdown and xdown - step_size >= i.x and ydown - step_size >= i.y:
                collision = True
                print("COLLIDING")
    elif direction == "down":
        for i in collider_list:
            if ydown + step_size <= i.ydown and xdown + step_size <= i.xdown and xdown + step_size >= i.x and ydown + step_size >= i.y:
                collision = True
                print("COLLIDING")




    return collision



class Collider():
    def __init__(self, parent, x, y, xdown, ydown):
        global collider_list
        self.parent = parent
        self.x = x
        self.y = y
        self.xdown = xdown
        self.ydown = ydown

        self.width = xdown - x
        self.height = ydown - y

        print(f"Collider created at X:{x} Y:{y}, X1:{xdown} Y1:{ydown}, width:{self.width} height:{self.height}")

        collider_list.append(self)


