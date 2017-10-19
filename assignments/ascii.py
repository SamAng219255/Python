def main():
 for i in  range(256):
  c=chr(i)
  l=str(i)
  if(len(l)==1):
   l="00"+l
  elif(len(l)==2):
   l="0"+l
  print("[",l," : ",c,"]",sep = "",end = " ")
  if(i%8==7):
   print()

main()
