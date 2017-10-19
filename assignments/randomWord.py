from math import *
from random import randint

def finPri(num):
 primes=[2]
 for i in range(num):
  if(i>1):
   prime=1
   for pri in primes:
    if((i+1)%pri==0):
     prime=0
   if(prime==1):
     primes.append(i+1)
 return primes
def lcmTo(num):
 primes=finPri(num)
 final=1
 for pri in primes:
  final=final*(pri**floor(log(num,pri)))
 return final
def genWeights():
 charPrio=["e","a","r","i","o","t","n","s","l","c","u","d","p","m","h","g","b","f","y","w","k","v","x","z","j","q"]
 digrPrio=["th","he","an","in","er","on","re","ed","nd","ha","at","en","es","of","nt","ea","ti","to","io","le","is","ou","ar","as","de","rt","ve"]
 strtPrio=["t","th","ti","to","a","an","at","ar","as","i","in","io","is","s","o","on","ou","of","w","h","he","ha","b","c","m","f","p","d","de","r","re","l","le","e","er","ed","en","es","ea","g","n","nd","y","u","k","v","ve","j","q","x","z"]
 
 charTotal=lcmTo(len(charPrio))
 digrTotal=lcmTo(len(digrPrio))
 strtTotal=lcmTo(len(digrPrio))
 charPrioNum=[]
 for i in range(1,len(charPrio)+1):
  charPrioNum.append(charTotal/i)
 digrPrioNum=[]
 for i in range(1,len(digrPrio)+1):
  digrPrioNum.append(digrTotal/i)
 strtPrioNum=[]
 for i in range(1,len(strtPrio)+1):
  strtPrioNum.append(strtTotal/i)
 digrCharPrioNum=[]
 for i in digrPrio:
  digrCharPrioNum.append((charPrioNum[charPrio.index(i[0])]*charPrioNum[charPrio.index(i[1])])**0.5)
 
 for i in range(len(digrPrio)):
  digrPrioNum[i]=(digrTotal*digrPrioNum[i]*digrCharPrioNum[i]/charTotal)**0.5
 
 return strtTotal, strtPrio, strtPrioNum, charTotal, charPrio, charPrioNum, digrTotal, digrPrio, digrPrioNum

def newCharacter(charTotal, charPrio, charPrioNum, digrTotal, digrPrio, digrPrioNum):
 putout=""
 if randint(1,3)==1:
  charPos=randint(0,digrTotal)
  for i in range(1,len(digrPrioNum)+1):
   if i==len(digrPrioNum):
    putout=digrPrio[i-1]
    break
   elif digrPrioNum[i] > charPos:
    putout=digrPrio[i-1]
    break
 else:
  charPos=randint(0,charTotal)
  for i in range(1,len(charPrioNum)+1):
   if i==len(charPrioNum):
    putout=charPrio[i-1]
    break
   elif charPrioNum[i] > charPos:
    putout=charPrio[i-1]
    break
 return putout

def genWordoid():
 strtTotal, strtPrio, strtPrioNum, charTotal, charPrio, charPrioNum, digrTotal, digrPrio, digrPrioNum = genWeights()
 total=""
 charPos=randint(0,strtTotal)
 for i in range(1,len(strtPrioNum)+1):
  if i==len(strtPrioNum):
   total+=strtPrio[i-1]
   break
  elif strtPrioNum[i] > charPos:
   total+=strtPrio[i-1]
   break
 wordLength=randint(0,5)
 keepGoing=True
 while keepGoing:
  keepGoing=False
  if randint(0,int(wordLength**0.5))>3:
   wordLength+=1
   keepGoing=True
 for i in range(wordLength):
  total+=newCharacter(charTotal, charPrio, charPrioNum, digrTotal, digrPrio, digrPrioNum)
 return total

print(genWordoid())
