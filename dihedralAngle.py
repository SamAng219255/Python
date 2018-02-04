from math import cos,sin
from math import acos as arccos
def csc(x):
	return 1/sin(x);
from matrix import *
def cross(*args):
	a=[0]*(len(args)+1)
	mat=[[0]*(len(args)+1) for i in range(len(args)+1)]
	for i in range(1,len(args)+1):
		for j in range(len(args)+1):
			mat[i][j]=args[i-1][j];
	for i in range(len(args)+1):
		a[i]=matrixDet(findMinorMat(0,i,mat))*(1-2*(i%2))
	return a
def dot(v1,v2):
	total=0;
	for i in range(len(v1)):
		total+=v1[i]*v2[i];
	return total;
def norm(v):
	total=0
	for i in v:
		total+=i**2
	return total**0.5
def vecangle(u,v):
	return acos(dot(u,v)/(norm(u)*norm(v)))
def unitVec(v):
	m=norm(v)
	V=[0]*len(v)
	for i in range(len(v)):
		V[i]=v[i]/m
	return V
pi=3.141592653589793238462643383279502884197169
def sqrt(x):
	return x**0.5

def diangle(n,n1):
	v1=[cos(pi*(n-2)/(2*n)),sin(pi*(n-2)/(2*n)),0]
	v2=[cos(pi*(n-2)/(2*n)),-sin(pi*(n-2)/(2*n)),0]
	v3=[sin(pi*(n1-2)/(2*n1))*csc(pi/n),0,sqrt(1-(sin(pi*(n1-2)/(2*n1))*csc(pi/n))**2)]
	u=cross(v1,v3)
	v=cross(v2,v3)
	return arccos(dot(u,v)/(norm(u)*norm(v)))

if __name__=='__main__':
	import sys
	print(0.001*round(180000*diangle(int(sys.argv[1]),int(sys.argv[2]))/pi))
