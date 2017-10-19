from random import randint
for i in range(66):
 print(bytes("\\033["+str(i)+"m"+str(i)+chr(randint(65,90)+(32*randint(0,1)))+"\\033[0m ","utf-8").decode("unicode_escape"),end="")
print()
