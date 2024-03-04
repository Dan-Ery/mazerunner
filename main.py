
from window import Window
from maze import Maze
def main():
    win = Window(800, 600)

    Maze(5,5,3,5,30,20,win)

    win.wait_for_close()

main()
