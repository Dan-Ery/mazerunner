"""Module providing functionality for Mazes."""
import random
import time
from cell import Cell

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
        seed = None
    ):
        self.x1=x1
        self.y1=y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.window=win

        if not seed is None:
            random.seed(seed)

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
