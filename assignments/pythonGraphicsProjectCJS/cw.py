from graphics import *


def main(win):
	win.yUp()
	
	rect = Rectangle(Point(300, 300), Point(100, 100))
	rect.setFill("yellow")
	rect.draw(win)
	
	eye1= Circle(Point(160, 230), 20)
	eye1.setFill("black")
	eye1.draw(win)
	
	eye2 = Circle(Point(240, 230), 20)
	eye2.setFill("black")
	eye2.draw(win)
	
	mouth = Line(Point(180, 180), Point(230, 180))
	mouth.setFill("black")
	mouth.draw(win)

	win.promptClose(win.getWidth()/2, 30)
	
