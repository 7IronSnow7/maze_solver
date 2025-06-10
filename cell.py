from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        if self._win is None:
            return
        
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line= Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")
            
    def draw_move(self, to_cell, undo=False):
        center_point_x_start = (self._x1 + self._x2) / 2
        center_point_y_start = (self._y1 + self._y2) / 2
        center_point_start = Point(center_point_x_start, center_point_y_start)

        center_point_x_end = (to_cell._x1 + to_cell._x2) / 2
        center_point_y_end = (to_cell._y1 + to_cell._y2) / 2
        center_point_end = Point(center_point_x_end, center_point_y_end)
        
        line = Line(center_point_start, center_point_end)
        color = "gray" if undo else "red"
        
        if self._win is None:
            return
        self._win.draw_line(line, color)
                