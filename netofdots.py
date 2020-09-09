from tkinter import *
from time import sleep
from parameters import *
from random import randint, choice, random


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

    def animation(self):
        x_velo = self._random_velo()
        y_velo = self._random_velo()

        while True:
            sleep(REFRESH_TIME)
            self.canvas.move(self.point1, x_velo, y_velo)
            self.canvas.update()

    def _random_velo(self):
        span = POINT_VELO_TO - POINT_VELO_FROM
        value_per_sec = POINT_VELO_FROM + random() * span
        value = value_per_sec * REFRESH_TIME
        sign = choice((-1, 1))
        return sign * value

    def run(self):
        self.root.after(0, self.animation)
        self.root.mainloop()


if __name__ == '__main__':
    nod = NetOfDots()
    nod.run()
