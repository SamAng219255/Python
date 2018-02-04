from math import log2

def spot(Pos):
 total=False
 mx=0
 for i in Pos:
  mx=max(mx,abs(int(i)))
 if mx>0:
  N=int(log2(mx))+1
 else:
  N=1
 for n in range(N,0,-1):
  for i in Pos:
   place=int(i)%(2**int(n))
   if place>=2**(int(n)-1):
    total=not total
   #print(n,i,total)
 return total

if __name__=='__main__':
 import sys
 print(spot(sys.argv[1].split(",")))
