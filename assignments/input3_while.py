print("INPUT THREE NUMBERS")
A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))
x=-5
while x<=5:
   y = A*x**2 + B*x + C
   print("({},{})".format(x,y))
   x+=1
