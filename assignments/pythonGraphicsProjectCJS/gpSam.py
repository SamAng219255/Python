import time
import copy
from graphics import *

def move(direc,x,y):
 newDirec=direc%4
 X=x
 if(newDirec==0):
  X+=3
 elif(newDirec==2):
  X+=-3
 Y=y
 if(newDirec==1):
  Y+=3
 elif(newDirec==3):
  Y+=-3
 return X,Y

def main(win):
 #win = GraphWin("PROJECT", 1536, 768)
 
 dragonList=[]
 dragonPoints=[]
 for i in range(16):
  temp=list(dragonList)
  dragonList.append(1)
  for i in range(len(temp)):
   dragonList.append(not temp[len(temp)-1-i])
 X=256
 Y=512
 direction=0
 dragonPoints.append(Point(X,Y))
 for turn in dragonList:
  X,Y=move(direction,X,Y)
  direction+=(turn*2)-1
  dragonPoints.append(Point(X,Y))
 skipFirst=0
 oldPoint=Point(0,0)
 tail=[]
 for i in range(len(dragonPoints)):
  if(skipFirst):
   tail.append(Line(oldPoint,dragonPoints[i]))
   tail[i-1].setWidth(1)
   tail[i-1].draw(win)
  else:
   skipFirst=1
  oldPoint=copy.deepcopy(dragonPoints[i])
  if(i%200==0):
   if win.checkMouse() is not None:
    win.close()
    break
 
 #if(win.isOpen()):
 # win.getMouse()
 # win.close()

#main()
