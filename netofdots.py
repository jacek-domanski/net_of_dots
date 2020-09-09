from tkinter import *
from time import sleep
from parameters import *
from point import Point
from random import randint, choice, random


class NetOfDots(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.points = self._create_points()
        self.canvas.pack()

    def _create_points(self):
        points = []
        for _ in range(NO_OF_POINTS):
            points.append(Point(self.canvas))

        return points

    def animation(self):
        while True:
            sleep(REFRESH_TIME)

            for pt in self.points:
                self.canvas.move(pt.point, pt.x_velo, pt.y_velo)
            self.canvas.update()

    def run(self):
        self.root.after(0, self.animation)
        self.root.mainloop()


if __name__ == '__main__':
    nod = NetOfDots()
    nod.run()
