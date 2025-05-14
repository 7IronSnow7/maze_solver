from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    
    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, "black")
    
    l2 = Line(Point(50, 50), Point(50, 400))
    win.draw_line(l2, "red")
    
    l3 = Line(Point(50, 400), Point(400, 400))
    win.draw_line(l3, "black")
    
    
    win.wait_for_close() 
    
main()