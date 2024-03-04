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



def main():
    win = Window(800, 600)
    win.wait_for_close()

main()
