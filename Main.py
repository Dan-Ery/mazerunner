from Window import *

def main():
    win = Window(800, 600)

    point_a, point_b = Point(0,0), Point(10,10)
    line = Line(point_a, point_b)
    win.draw_line(line, "red")

    win.wait_for_close()

main()
