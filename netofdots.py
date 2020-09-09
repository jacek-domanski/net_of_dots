from tkinter import *
from time import sleep
from parameters import *
from random import randint


class NetOfDots(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.point1 = self._create_circle(self.canvas,
                                          randint(POINT_RADIUS, CANVAS_WIDTH-POINT_RADIUS),
                                          randint(POINT_RADIUS, CANVAS_WIDTH-POINT_RADIUS),
                                          POINT_RADIUS,
                                          fill='black')
        self.canvas.pack()

    def _create_circle(self, canvas, x, y, r, **kwargs):
        return canvas.create_oval(x-r, y-r, x+r, y+r, kwargs)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    nod = NetOfDots()
    nod.run()
