from tkinter import *
from time import sleep
from parameters import *


class NetOfDots(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    nod = NetOfDots()
    nod.run()
