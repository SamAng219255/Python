import gpSam as psa
import jrs as jrs
import cw as cw

from graphics import *

while True:
 win = GraphWin("PROJECT", 1536, 768)
 psa.main(win)
 if(win.isOpen()):
  win.getMouse()
  win.close()
 win = GraphWin("Draw an Octagon", 350, 350)
 jrs.main(win)
 if(win.isOpen()):
  win.getMouse()
  win.close()
 win = GraphWin("CW", 400, 400)
 cw.main(win)
 if(win.isOpen()):
  win.getMouse()
  win.close()
