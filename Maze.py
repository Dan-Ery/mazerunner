from Window import *

class Cell:
    def __init__(self, win):
        self.window=win

        self.has_left_wall=True
        self.has_right_wall=True
        self.has_top_wall=True
        self.has_bottom_wall=True

        self.x1=None
        self.y1=None
        self.x2=None
        self.y2=None
    
    def draw(self, x1, y1, x2, y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.window.draw_line(line, "black")
            
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self.window.draw_line(line, "black")
            
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.window.draw_line(line, "black")
            
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.window.draw_line(line, "black")