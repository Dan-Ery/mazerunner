import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(
            m1.cells[0][0].has_top_wall
        )
        self.assertFalse(
            m1.cells[num_cols - 1][num_rows - 1].has_bottom_wall
        )
    
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in range(0,num_cols):
            for row in range(0,num_rows):
                m1.cells[0][0].visited = True
        m1._reset_cells_visited()

        for col in range(0,num_cols):
            for row in range(0,num_rows):
                self.assertFalse(
                    m1.cells[0][0].visited
                )


if __name__ == "__main__":
    unittest.main()