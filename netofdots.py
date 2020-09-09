from tkinter import *
from time import sleep
from parameters import *
from point import Point


class NetOfDots(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.points = self._create_points()
        self.lines = []
        self.canvas.pack()

    def _create_points(self):
        points = []
        for _ in range(NO_OF_POINTS):
            points.append(Point(self.canvas))

        return points

    def animation(self):
        while True:
            sleep(REFRESH_TIME)

            for i, pt in enumerate(self.points):
                self.canvas.move(pt.point, pt.x_velo, pt.y_velo)
                self.replace_point_if_out_of_canvas(i, pt)

            self.draw_lines_between_close_points()

            self.canvas.update()

    def draw_lines_between_close_points(self):
        self.remove_all_lines()

        for i, point_a in enumerate(self.points[:-1]):
            for point_b in self.points[i:]:
                if point_a-point_b <= MAX_LINE_LENGTH:
                    self.draw_line_between_points(point_a, point_b)

    def remove_all_lines(self):
        for line in self.lines:
            self.canvas.delete(line)

        self.lines = []

    def draw_line_between_points(self, a: Point, b: Point):
        line = self.canvas.create_line(a.get_x(), a.get_y(), b.get_x(), b.get_y())
        self.lines.append(line)

    def replace_point_if_out_of_canvas(self, i, pt):
        if pt.is_out_of_canvas():
            self.canvas.delete(pt.point)
            del self.points[i]
            self.points.append(Point(self.canvas))

    def run(self):
        self.root.after(0, self.animation)
        self.root.mainloop()


if __name__ == '__main__':
    nod = NetOfDots()
    nod.run()
