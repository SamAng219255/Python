from copy import copy, deepcopy
from math import acos
def matrixDet(matRiX):
	matriX=deepcopy(matRiX)
	matLength=len(matriX)
	tempDet=0
	if(matLength==len(matriX[0])):
		if(matLength!=2 and matLength!=1 and matLength!=0):
			try:
				tempDet=0
				sign=1
				for i in range(matLength):
					newMat=findMinorMat(0,i,matriX)
					tempDet+=sign*matrixDet(newMat)*matriX[0][i]
					sign*=-1
			except:
				tempDet=None
		elif(matLength==2):
			tempDet=(matriX[0][0]*matriX[1][1])-(matriX[0][1]*matriX[1][0])
		elif(matLength==1):
			tempDet=matriX[0][0]
		else:
			tempDet=None
	else:
		tempDet=None
	return tempDet
def findMinorMat(I,J,mat):
	temp=deepcopy(mat)
	temp.pop(I)
	for i in range(len(temp)):
		temp[i].pop(J)
	return temp
def matrixInv(matrIX):
	det=matrixDet(matrIX)
	if(len(matrIX)==len(matrIX[0]) and det!=0 and det!=None):
		if len(matrIX)==1:
			return [[1/matrIX[0][0]]]
		elif len(matrIX)==2:
			return [[matrIX[1][1]/det,-matrIX[0][1]/det],[-matrIX[1][0]/det,matrIX[0][0]/det]]
		elif len(matrIX)==3:
			pos=[
			[[[(2,2),(2,3)],[(3,2),(3,3)]],[[(1,3),(1,2)],[(3,3),(3,2)]],[[(1,2),(1,3)],[(2,2),(2,3)]]],
			[[[(2,3),(2,1)],[(3,3),(3,1)]],[[(1,1),(1,3)],[(3,1),(3,3)]],[[(1,3),(1,1)],[(2,3),(2,1)]]],
			[[[(2,1),(2,2)],[(3,1),(3,2)]],[[(1,2),(1,1)],[(3,2),(3,1)]],[[(1,1),(1,2)],[(2,1),(2,2)]]]
			]
			matRIX=[[0]*3 for i in range(3)]
			for i in range(3):
				for j in range(3):
					tempMat=[[0]*2 for i in range(2)]
					for k in range(2):
						for l in range(2):
							I,J=pos[i][j][k][l]
							tempMat[k][l]=matrIX[I-1][J-1]
					matRIX[i][j]=matrixDet(tempMat)/det
			return matRIX
	else:
		return None
def matrixMulti(matrix1,matrix2):
	matrix3=[[0]*len(matrix2[0]) for i in range(len(matrix1))]
	for i in range(len(matrix1)):
		for j in range(len(matrix2[0])):
			for k in range(len(matrix1[0])):
				matrix3[i][j]+=matrix1[i][k]*matrix2[k][j]
	return matrix3
def identity(degree):
	total=[[0]*degree for i in range(degree)]
	for i in range(degree):
		total[i][i]=1
	return total
def matrixAdd(matrix1,matrix2):
	if len(matrix1)==len(matrix2) and len(matrix1[0])==len(matrix2[0]):
		matrix3=[[0]*len(matrix2[0]) for i in range(len(matrix1))]
		for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
		return matrix3
	else:
		return None
def matrixSub(matrix1,matrix2):
	if len(matrix1)==len(matrix2) and len(matrix1[0])==len(matrix2[0]):
		matrix3=[[0]*len(matrix2[0]) for i in range(len(matrix1))]
		for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				matrix3[i][j]=matrix1[i][j]-matrix2[i][j]
		return matrix3
	else:
		return None
def matrixMultiScal(matrix1,num):
	matrix2=[[0]*len(matrix1[0]) for i in range(len(matrix1))]
	for i in range(len(matrix1)):
		for j in range(len(matrix1[0])):
			matrix2[i][j]=matrix1[i][j]*num
	return matrix2
def sksycrpr(matrix1):
	return [[0,-matrix1[2],matrix1[1]],[matrix1[2],0,-matrix1[0]],[-matrix1[1],matrix1[0],0]]
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
