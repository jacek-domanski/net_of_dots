from tkinter import *
from parameters import *
from random import randint, choice, random


class Point(object):
    def __init__(self, canvas: Canvas):
        self.point = self.__create_circle(canvas,
                                          randint(POINT_RADIUS, CANVAS_WIDTH - POINT_RADIUS),
                                          randint(POINT_RADIUS, CANVAS_WIDTH - POINT_RADIUS),
                                          POINT_RADIUS,
                                          fill='black')
        self.x_velo = self.__random_velo()
        self.y_velo = self.__random_velo()

    @staticmethod
    def __create_circle(canvas, x, y, r, **kwargs):
        return canvas.create_oval(x - r, y - r, x + r, y + r, kwargs)

    @staticmethod
    def __random_velo():
        span = POINT_VELO_TO - POINT_VELO_FROM
        value_per_sec = POINT_VELO_FROM + random() * span
        value = value_per_sec * REFRESH_TIME
        sign = choice((-1, 1))
        return sign * value
