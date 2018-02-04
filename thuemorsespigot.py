from math import log2
def thmo(num):
 x=num
 n=0
 while(x>0):
  temp=int(log2(x))
  x-=2**temp
  n+=1
 return int(n%2==1)

if __name__=='__main__':
 import sys
 print(thmo(int(sys.argv[1])))
