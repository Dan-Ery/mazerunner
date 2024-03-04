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
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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

    def _break_walls_r(self, col, row):
        current_cell : Cell = self.cells[col][row]
        current_cell.visited = True

        is_dead_end = False
        while not is_dead_end:
            available_directions = []
            if col > 0 and self.cells[col-1][row].visited is False:
                available_directions.append(1)
            if col < self.num_cols-1 and self.cells[col+1][row].visited is False:
                available_directions.append(2)
            if row > 0 and self.cells[col][row-1].visited is False:
                available_directions.append(3)
            if row < self.num_rows-1 and self.cells[col][row+1].visited is False:
                available_directions.append(4)

            if available_directions:
                direction_index = random.randrange(len(available_directions))
                direction = available_directions[direction_index]
                match direction:
                    case 1:
                        current_cell.has_left_wall=False
                        self.cells[col-1][row].has_right_wall = False
                        self._draw_cell(col, row)
                        self._break_walls_r(col-1,row)
                    case 2:
                        current_cell.has_right_wall=False
                        self.cells[col+1][row].has_left_wall = False
                        self._draw_cell(col, row)
                        self._break_walls_r(col+1,row)
                    case 3:
                        current_cell.has_top_wall = False
                        self.cells[col][row-1].has_bottom_wall = False
                        self._draw_cell(col, row)
                        self._break_walls_r(col,row-1)
                    case 4:
                        current_cell.has_bottom_wall = False
                        self.cells[col][row+1].has_top_wall = False
                        self._draw_cell(col, row)
                        self._break_walls_r(col,row+1)
            else:
                self._draw_cell(col, row)
                is_dead_end = True

    def _reset_cells_visited(self):
        for col in range(0, self.num_cols):
            for row in range(0, self.num_rows):
                self.cells[col][row].visited = False

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, col, row):
        self._animate()

        current_cell : Cell = self.cells[col][row]
        current_cell.visited = True
        if col == self.num_cols-1 and row == self.num_rows-1:
            return True

        if self._solve_left(col, row):
            return True
        if self._solve_right(col, row):
            return True
        if self._solve_up(col, row):
            return True
        if self._solve_down(col, row):
            return True
        return False

    def _solve_left(self, col, row):
        current_cell : Cell = self.cells[col][row]
        if col > 0 and not current_cell.has_left_wall:
            left_cell : Cell = self.cells[col-1][row]
            if left_cell.visited is False:
                current_cell.draw_move(left_cell, False)
                if self._solve_r(col-1, row):
                    return True
                current_cell.draw_move(left_cell, True)
        return False

    def _solve_right(self, col, row):
        current_cell : Cell = self.cells[col][row]
        if col < self.num_cols-1 and not current_cell.has_right_wall:
            right_cell : Cell = self.cells[col+1][row]
            if right_cell.visited is False:
                current_cell.draw_move(right_cell, False)
                if self._solve_r(col+1, row):
                    return True
                current_cell.draw_move(right_cell, True)
        return False

    def _solve_up(self, col, row):
        current_cell : Cell = self.cells[col][row]
        if row > 0 and not current_cell.has_top_wall:
            above_cell : Cell = self.cells[col][row-1]
            if above_cell.visited is False:
                current_cell.draw_move(above_cell, False)
                if self._solve_r(col, row-1):
                    return True
                current_cell.draw_move(above_cell, True)
        return False

    def _solve_down(self, col, row):
        current_cell : Cell = self.cells[col][row]
        if row < self.num_rows-1 and not current_cell.has_bottom_wall:
            below_cell : Cell = self.cells[col][row+1]
            if below_cell.visited is False:
                current_cell.draw_move(below_cell, False)
                if self._solve_r(col, row+1):
                    return True
                current_cell.draw_move(below_cell, True)
        return False
