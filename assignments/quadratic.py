def roots(a,b,c):
 d=b**2-4*a*c
 if d!=0:
  return 2,[(-b+(d**0.5))/(2*a),(-b-(d**0.5))/(2*a)]
 elif d==0:
  return 1,[(-b+(d**0.5))/(2*a)]

if __name__ == '__main__':
 a=float(input('A: '))
 b=float(input('B: '))
 c=float(input('C: '))
 leng,val=roots(a,b,c)
 if(leng==2):
  print('x1: {}\nx2: {}'.format(val[0],val[1]))
 elif(leng==1):
  print('x: {}'.format(val[0]))
