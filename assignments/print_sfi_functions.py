def intcalc(x,y):
   return x*y
def floatcalc(x,y):
   return x/y
def stringcat(x,y):
   return x+y
def main():
   print "{}, {}, {}".format(stringcat("hello ","world"), floatcalc(9.,2.), intcalc(2,3))

main()
