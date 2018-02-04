from math import log

chars=list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
charstwo=list("0123456789abcdef")
def baseConv(init,basestart,baseend):
 baseten=0
 if basestart<=36:
  initi=init.lower()
 else:
  initi=init
 for i in range(0,len(initi)):
  baseten+=chars.index(initi[len(initi)-1-i])*(basestart**i)
 total=""
 size=int(log(baseten,baseend))
 for i in range(size,-1,-1):
  total+=charstwo[baseten//(baseend**i)]
  baseten%=(baseend**i)
 return total

if __name__=='__main__':
 import sys
 print(baseConv(sys.argv[1],53,int(sys.argv[2])))
