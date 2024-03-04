from Window import *
from Maze import *
def main():
    win = Window(800, 600)

    maze = Maze(5,5,3,5,30,20,win)

    win.wait_for_close()

main()
