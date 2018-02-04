import math
import random
from primesviaopenssl import getPrimes

def chop(text,size):
 txt=lengthen(text,math.ceil(len(text)/size)*size)
 chopped=[]
 length=len(txt)
 for i in range(length):
  if (length-i)%size==0:
   chopped.append("")
  chopped[len(chopped)-1]+=txt[i]
 return chopped

def lengthen(txt,size):
 return ("0"*(size-len(txt)))+txt

def test_pri(n,k): #Very Slow
 #(2**r)*d=n-1
 r=0
 d=n-1
 while d%2==0:
  r+=1
  d=d//2
 for i in range(k):
  a=random.randint(2,n-2)
  x=a**d % n
  Continue=False
  if (x==1) or (x==n-1):
   continue
  for i in range(r-1):
   x=(x**2)%n
   if x==1:
    return False
   if x==n-1:
    Continue=True
    break
  if Continue:
   continue
  return False
 return True
 """Input #1: n > 3, an odd integer to be tested for primality;
 Input #2: k, a parameter that determines the accuracy of the test
 Output: composite if n is composite, otherwise probably prime
 
 write n − 1 as 2**r·d with d odd by factoring powers of 2 from n − 1
 WitnessLoop: repeat k times:
    pick a random integer a in the range [2, n − 2]
    x ← a**d mod n
    if x = 1 or x = n − 1 then
       continue WitnessLoop
    repeat r − 1 times:
       x ← x**2 mod n
       if x = 1 then
          return composite
       if x = n − 1 then
          continue WitnessLoop
    return composite
 return probably prime"""

def inverse(a, n):
    t = 0;     newt = 1;    
    r = n;     newr = a;    
    while newr != 0:
        quotient = int(r/newr)
        (t, newt) = (newt, t - quotient * newt) 
        (r, newr) = (newr, r - quotient * newr)
    if r > 1:
        return "a is not invertible"
    if t < 0:
        t = t + n
    return t

def encryptshort(m,e,n):
 return (m**e)%n

def decryptshort(c,d,n):
 return (c**d)%n

def encrypt(m,e,n):
 if(m>n):
  total=""
  newms=chop(str(m),len(str(n))-1)
  for shortened in newms:
   total+=lengthen(str(encryptshort(int(shortened),e,n)),len(str(n))-1)
  return int(total)
 else:
  return encryptshort(m,e,n)

def decrypt(c,d,n):
 if(c>n):
  total=""
  newms=chop(str(c),len(str(n))-1)
  for shortened in newcs:
   total+=lengthen(str(encryptshort(int(shortened),d,n)),len(str(n))-1)
  return int(total)
 else:
  return decryptshort(c,d,n)

def genKeys(p,q):
 total={"n":p*q}
 gcd=2
 while gcd!=1:
  rand=random.randint(int(math.log2(total["n"])**0.5),int(math.log2(total["n"])))
  gcd=math.gcd((p-1)*(q-1),rand)
 total["e"]=rand
 total["d"]=inverse(total["e"],(p-1)*(q-1))
 return total

def randPrime(a,b): #Very Slow
 isntPrime=True
 while isntPrime:
  rand=random.randint(int((a-(a&2))//2),int((b-(b&2))//2))*2+11
  isntPrime=not test_pri(rand,1000)
 return rand
