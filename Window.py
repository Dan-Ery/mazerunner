from tkinter import Tk, BOTH, Canvas
class Window:
    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.wm_title("root")
        self.canvas = Canvas()
        self.canvas.pack()
        self.running=False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running=True
        while self.running:
            self.redraw()

    def close(self):
        self.running=False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
class Line:
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill_color, 2)