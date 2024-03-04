from Window import *
from Maze import *
def main():
    win = Window(800, 600)

    point_a, point_b = Point(0,0), Point(10,10)
    cell = Cell(win)
    cell.draw(5,5,40,40)

    win.wait_for_close()

main()
