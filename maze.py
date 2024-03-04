"""Module providing functionality for Mazes."""
import time
from window import Point, Line

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.window=win

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        cell_matrix = []
        for col in range(0, self.num_cols):
            column = []
            for row in range(0, self.num_rows):
                cell = Cell(self.window)
                column.append(cell)
            cell_matrix.append(column)

        self.cells = cell_matrix

        for col in range(0, self.num_cols):
            for row in range(0, self.num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self.window is None:
            return
        x1 = self.x1 + self.cell_size_x * col
        x2 = x1 + self.cell_size_x
        y1 = self.y1 + self.cell_size_y * row
        y2 = y1+ self.cell_size_y

        cell = self.cells[col][row]
        cell.draw(x1,y1,x2,y2)
        self._animate()

    def _animate(self):
        window = self.window
        if not window is None:
            window.redraw()
            time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entry_cell = self.cells[0][0]
        exit_cell = self.cells[self.num_cols - 1][self.num_rows - 1]
        entry_cell.has_top_wall=False
        exit_cell.has_bottom_wall=False
        self._draw_cell(0, 0)
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

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
