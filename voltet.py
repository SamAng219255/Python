from matrix import *

J=1j

def cross(b,c):
	a=[(b[1]*c[2]-b[2]*c[1]),(b[2]*c[0]-b[0]*c[2]),(b[0]*c[1]-b[1]*c[0])]
	return a
def dot(v1,v2):
	return matrixMulti([[v1[0],v1[1],v1[2]]],[[v2[0]],[v2[1]],[v2[2]]])[0][0]
def norm(v):
	return sqrt(v[0]**2+v[1]**2+v[2]**2)
def sqrt(x):
	return x**0.5
def unitVec(v):
	m=sqrt(v[0]**2+v[1]**2+v[2]**2)
	return [v[0]/m,v[1]/m,v[2]/m]
def alignVectors(v1,v2):
	V1,V2=unitVec(v1),unitVec(v2)
	v=cross(V1,V2)
	s=norm(v)
	c=dot(V1,V2)
	R=matrixAdd(matrixAdd(identity(3),sksycrpr(v)),matrixMultiScal(matrixMulti(sksycrpr(v),sksycrpr(v)),1/(1+c)))
	return R
def distance(p1,p2):
	return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)**0.5
def line2point(p1,p2,p3):
	a,b,c=distance(p1,p2),distance(p2,p3),distance(p3,p1)
	cosA,cosB,cosC=(b**2+c**2-a**2)/(2*b*c),(a**2+c**2-b**2)/(2*a*c),(a**2+b**2-c**2)/(2*a*b)
	sinA,sinB,sinC=sqrt(1-cosA**2),sqrt(1-cosB**2),sqrt(1-cosC**2)
	return c*sinB
def plane2point(p1,p2,p3,p4):
	mat=[p1.copy(),p2.copy(),p3.copy()]
	newmat=matrixInv(mat)
	res=matrixMulti(newmat,[[1],[1],[1]])
	a,b,c,d=res[0][0],res[1][0],res[2][0],1
	print(a,b,c,d)
	return abs(a*p4[0]+b*p4[1]+c*p4[2]-d)/sqrt(a**2+b**2+c**2)
def volume(p1,p2,p3,p4):
	return distance(p1,p2)*line2point(p1,p2,p3)*plane2point(p1,p2,p3,p4)/6