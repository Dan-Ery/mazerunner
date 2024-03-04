from Window import *
from Maze import *
def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.draw(5,5,40,40)
    cell2 = Cell(win)
    cell2.draw(55,55,80,80)
    cell1.draw_move(cell2)

    win.wait_for_close()

main()
