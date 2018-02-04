import json

f=open("primes","r")
primes=json.load(f)
f.close()

def find_factors(num):
	factors=[0]*len(primes)
	pos=0
	if num in primes:
		pos=primes.index(num)
		factors[pos]=1
	else:
		divisor=1
		numb=int(num)
		if(num%1!=0):
			if(len(str(num))==19):
				temp=0.000000001
				count=0
				while temp%1!=0 and count<19:
					count+=1
					temp=num*int("9"*count)
				divisor=int("9"*count)
				numb=int(temp)
			else:
				divisor=10**(len(str(num))-2)
				numb=int(num*divisor)
		if numb in primes:
			pos=primes.index(numb)
			factors[pos]=1
		else:
			multiple=1
			pos=0
			going=True
			while going:
				if(numb%primes[pos]==0):
					while numb/multiple%primes[pos]==0:
						factors[pos]+=1
						multiple*=primes[pos]
				if(multiple==1):
					going=numb**0.5>primes[pos]
				else:
					going=numb/multiple>primes[pos]
				pos+=1
		if(divisor!=1):
			inverseFactors=find_factors(divisor)
			for i in range(len(inverseFactors)):
				factors[i]-=inverseFactors[i]
	highest=0
	for i in range(len(factors)):
		if factors[i]!=0:
			highest=i
	return factors[0:highest+1]

def div_odd(num):
	return find_factors(num)[0]

def dict_factors(num):
	factors=find_factors(num)
	newFactors={}
	for i in range(len(factors)):
		if factors[i]!=0:
			newFactors[str(primes[i])]=factors[i]
	return newFactors

if __name__=='__main__':
	import sys
	print(dict_factors(int(sys.argv[1])))
