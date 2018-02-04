#import json
#primes=json.load("primes")

def pnl(lst):
 total=lst.split(",")
 for i in range(len(total)):
  total[i]=int(total[i])
 return total

def reorgnew(co,mod,it):
 temp=[]
 stor=[]
 for i in range(mod):
  temp.append((i*co)%mod)
 stor=list(temp)
 for n in range(it-1):
  for i in range(mod):
   stor[i]=temp[stor[i]]
 return stor

def reorg(lst,co,mod,it):
 stor=list(lst)
 for n in range(it):
  for i in range(len(stor)):
   stor[i]=(stor[i]*co)%mod
 return stor

#8000000011 5656854251 3313708499
def randorg(inp):
 if(type(inp)==list):
  stor=list(lst)
  for n in range(7):
   for i in range(len(stor)):
    stor[i]=(stor[i]*5656854251)%8000000011
  for n in range(7):
   for i in range(len(stor)):
    stor[i]=(stor[i]*3313708499)%8000000011
 elif(type(inp)==int):
  stor=inp
  for i in range(7):
   stor=(stor*5656854251)%8000000011
  for i in range(7):
   stor=(stor*3313708499)%8000000011
 return stor

if __name__=='__main__':
 import sys
 print(randorg(int(sys.argv[1])))
