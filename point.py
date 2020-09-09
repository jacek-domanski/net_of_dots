from tkinter import *
from parameters import *
from random import randint, choice, random
from math import sqrt


class Point(object):
    def __init__(self, canvas: Canvas):
        self.canvas = canvas
        self.point = self.__create_circle(randint(POINT_RADIUS, CANVAS_WIDTH - POINT_RADIUS),
                                          randint(POINT_RADIUS, CANVAS_WIDTH - POINT_RADIUS),
                                          POINT_RADIUS,
                                          fill=COLOR,
                                          outline=COLOR)
        self.x_velo = self.__random_velo()
        self.y_velo = self.__random_velo()

    def __create_circle(self, x, y, r, **kwargs):
        return self.canvas.create_oval(x - r, y - r, x + r, y + r, kwargs)

    @staticmethod
    def __random_velo():
        span = POINT_VELO_TO - POINT_VELO_FROM
        value_per_sec = POINT_VELO_FROM + random() * span
        value = value_per_sec * REFRESH_TIME
        sign = choice((-1, 1))
        return sign * value

    def is_out_of_canvas(self):
        x = self.get_x()
        y = self.get_y()

        return x < 0 or \
               y < 0 or \
               x > CANVAS_WIDTH or \
               y > CANVAS_HEIGHT

    def get_x(self):
        x0, y0, x1, y1 = self.canvas.coords(self.point)
        return (x0 + x1) / 2

    def get_y(self):
        x0, y0, x1, y1 = self.canvas.coords(self.point)
        return (y0 + y1) / 2

    def __sub__(self, other):
        dist_x = other.get_x() - self.get_x()
        dist_y = other.get_y() - self.get_y()

        return sqrt(pow(dist_x, 2) + pow(dist_y, 2))

