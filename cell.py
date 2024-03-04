from window import Line, Point


class Cell:
    def __init__(self, win):
        self.window=win

        self.has_left_wall=True
        self.has_right_wall=True
        self.has_top_wall=True
        self.has_bottom_wall=True

        self.x1=0
        self.y1=0
        self.x2=0
        self.y2=0

        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

        left = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self.window.draw_line(left, "black")
        else:
            self.window.draw_line(left, "white")

        right = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self.window.draw_line(right, "black")
        else:
            self.window.draw_line(right, "white")

        top = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self.window.draw_line(top, "black")
        else:
            self.window.draw_line(top, "white")

        bottom = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self.window.draw_line(bottom, "black")
        else:
            self.window.draw_line(bottom, "white")

    def get_center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return Point(center_x, center_y)

    def draw_move(self, to_cell, undo=False):
        line_color = "red"
        if undo:
            line_color = "gray"
        line = Line(self.get_center(), to_cell.get_center())
        self.window.draw_line(line, line_color)
