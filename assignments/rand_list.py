from random import randint

def randomStr(listed):
 alpha=listed
 total=""
 while(len(alpha)>0):
  total=total+alpha.pop(randint(0,len(alpha)-1))
 return total
def numLToChrL(numList):
 chrList=[]
 alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=~`[]\\{}|;':\",./<>?"
 for num in numList:
  chrList.append(alpha[num%len(alpha)])
 return chrList
def main():
 f=open("the_cliffs_of_insanity.txt","w")
 chars=int(input("How long should it be?\n"))
 turns=max(int(chars/94),1)
 for i in range(turns):
  ranged=range(94)
  if i==turns:
   ranged=range(chars%94)
  ranstr=randomStr(numLToChrL(ranged))
  print(ranstr,end="")
  f.write(ranstr)
 print()
 f.close()

main()
