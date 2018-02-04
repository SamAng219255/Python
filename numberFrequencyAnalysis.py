import random
import sys

total=[0]*10
totalp=[0]*10
primes=[2]
totalp[2]=1

def testNewPrime(x):
 prime=True
 i=0
 while i<len(primes) and i<x/2:
  p=primes[i]
  if x%p==0:
   prime=False
   primes.append(x)
   break
  i+=1
 return prime

for i in range(int(sys.argv[1])):
 for cha in str(i):
  total[int(cha)]+=1
 #if testNewPrime(i):
 # for cha in str(i):
 #  totalp[int(cha)]+=1

print("total",total)
