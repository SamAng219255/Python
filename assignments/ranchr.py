from random import randint

def rint():
 r = randint(65,90)
 r += 32*randint(0,1)
 return r
def main():
 for i in range(1000000):
  z=rint()
  print(chr(z),end="")

main()
