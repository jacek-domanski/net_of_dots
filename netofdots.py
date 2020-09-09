from tkinter import *
from time import sleep
from parameters import *
from random import randint, choice, random


class NetOfDots(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.points = self._create_points()
        self.x_velos = self.generate_random_velos()
        self.y_velos = self.generate_random_velos()
        self.canvas.pack()

    def _create_points(self):
        points = []
        for _ in range(NO_OF_POINTS):
            point = self._create_circle(self.canvas,
                                        randint(POINT_RADIUS, CANVAS_WIDTH - POINT_RADIUS),
                                        randint(POINT_RADIUS, CANVAS_WIDTH - POINT_RADIUS),
                                        POINT_RADIUS,
                                        fill='black')
            points.append(point)

        return points

    def _create_circle(self, canvas, x, y, r, **kwargs):
        return canvas.create_oval(x - r, y - r, x + r, y + r, kwargs)

    def animation(self):
        while True:
            sleep(REFRESH_TIME)
            for point, x_velo, y_velo in zip(self.points, self.x_velos, self.y_velos):
                self.canvas.move(point, x_velo, y_velo)
            self.canvas.update()

    def generate_random_velos(self):
        velos = []
        for _ in range(NO_OF_POINTS):
            velos.append(self._random_velo())

        return velos

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
