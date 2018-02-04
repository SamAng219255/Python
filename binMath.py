from math import ceil

def binAdd(*args):
 #print(len(args))
 x=args[0]
 y=args[1]
 if len(args)>3:
  if type(args[2])==bool:
   over=args[2]
   length=args[3]
  else:
   over=args[3]
   length=args[2]
 elif(len(args)>2):
  if type(args[2])==bool:
   over=args[2]
   length=ceil(max(len(x),len(y))/4)*4
  else:
   over=False
   length=args[2]
 else:
  over=False
  length=ceil(max(len(x),len(y))/4)*4
 #print(over,length)
 #print("x",x,"y",y)
 y=("0"*(length-len(y)))+y
 x=("0"*(length-len(x)))+x
 #print("x",x,"y",y)
 y=y[(len(y)-length):]
 x=x[(len(x)-length):]
 #print("x",x,"y",y)
 carry=0
 c=""
 z=""
 for i in range(length-1,-1,-1):
  #print(x,i)
  X=int(x[i])
  Y=int(y[i])
  z=str(int(X ^ Y ^ carry))+z
  carry=int((X and Y) or ((X or Y) and carry))
  c=str(carry)+c
 if over:
  z=str(int(carry))+z
 return z
def binMinus(*args):
 x=args[0]
 y=args[1]
 if len(args)>3:
  if type(args[2])==bool:
   over=args[2]
   length=args[3]
  else:
   over=args[3]
   length=args[2]
 elif(len(args)>2):
  if type(args[2])==bool:
   over=args[2]
   length=ceil(max(len(x),len(y))/4)*4
  else:
   over=False
   length=args[2]
 else:
  over=False
  length=ceil(max(len(x),len(y))/4)*4
 y=("0"*(length-len(y)))+y
 x=("0"*(length-len(x)))+x
 y=y[(len(y)-length):]
 x=x[(len(x)-length):]
 carry=0
 c=""
 z=""
 for i in range(length-1,-1,-1):
  X=int(x[i])
  Y=int(y[i])
  z=str(int(Y^carry^X))+z
  carry=(Y and carry) or (not X and (Y or carry))
  c=str(int(carry))+c
 return z

if __name__=='__main__':
 option=int(input("Choose an operation:\n 1): Addition\n 2): Subtraction\n"))
 num1=input("Enter first number:\n")
 num2=input("Enter second number:\n")
 if input("Set byte length?\n").lower() in ["yes","y","true","t","ja","j","si","s"]:
  length=int(input("Enter byte length:\n"))
 else:
  ceil(max(len(x),len(y))/4)*4
 over=input("Allow overflow?\n").lower() in ["yes","y","true","t","ja","j","si","s"]
 if option<=1:
  print("sum")
  print(binAdd(num1,num2))
 elif option<=2:
  print("difference")
  print(binMinus(num1,num2))
