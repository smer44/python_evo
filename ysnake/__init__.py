from graphics  import *


def main():
    win = GraphWin("My Window", 500,500)
    #top left is 0 0
    win.setBackground(color_rgb(0,0,0))
    pt = Point(250,250) # single pixel drawn
    cir = Circle(pt,50)
    
    cir.setFill(color_rgb(100,255,50))
    
    cir.draw(win)
    
    ln = Line(Point(250,250), Point(250,350))
    
    ln.setOutline(color_rgb(0,255,255))
    
    ln.draw(win)
    
    #win.getMouse()
    win.close()
    
#main()
    