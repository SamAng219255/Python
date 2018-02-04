from math import ceil

def rotcoord(x,y,n,s):
 X,Y=x,y
 for i in range(n%3):
  X,Y=int((Y+1)/2)+s-1-X,Y%2+2*(s-1-X)
 return X,Y
def idtocoord(x):
 return ceil((x+1)**0.5-1),x-ceil((x+1)**0.5-1)**2
def coordtoid(x,y):
 return x**2+y
class plate:
 regions=[]
 movement=[]
class planet:
 plates=[]