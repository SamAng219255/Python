from graphics import *

def main(win):
	win.yUp() # right side up coordinates
	win.setBackground('grey')
	message = Text(Point(win.getWidth()/2, 30), 'Click on eight points')
	message.setTextColor('blue')
	message.setStyle('italic')
	message.setSize(20)
	message.draw(win)

    # Get and draw 8 vertices of octagon
	p1 = win.getMouse()
	p1.draw(win)
	p2 = win.getMouse()
	p2.draw(win)
	p3 = win.getMouse()
	p3.draw(win)
	p4 = win.getMouse()
	p4.draw(win)
	p5 = win.getMouse()
	p5.draw(win)
	p6 = win.getMouse()
	p6.draw(win)
	p7 = win.getMouse()
	p7.draw(win)
	p8 = win.getMouse()
	p8.draw(win)
	vertices = [p1, p2, p3, p4, p5, p6, p7, p8]

    # Use Polygon object to draw the octagon
	octagon = Polygon(vertices)
	octagon.setFill('purple')
	octagon.setOutline('red')
	octagon.setWidth(4)  # width of boundary line
	octagon.draw(win)

	message.setText('Click anywhere to quit') # change text message
