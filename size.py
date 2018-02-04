from os import system as call
import sys

stuff=sys.argv[1].split(",")
print(stuff)
all=False

def size(thing):
 call("ls -lR "+thing+" | egrep ' root| samanguiano' > everthing")
 print("File List Generated")
 f=open("everthing")
 total=0
 for line in f:
  stuff=line.split(" ")
  i=4
  while True:
   try:
    while stuff[i]=="":
     i+=1
    total+=int(stuff[i])
   except ValueError:
    i+=1
    pass
   else:
    break
 f.close()
 print(thing,total)

for thing in stuff:
 if thing=="all":
  all=True
 elif all:
  call("ls -l "+thing+" | egrep ' root| samanguiano' > everthing")
  f=open("everthing")
  files=[]
  if thing[len(thing)-1]!="/":
   Thing=thing+"/"
  else:
   Thing=thing
  for line in f:
   files.append(Thing+line.split(" ")[len(line.split(" "))-1])
  f.close()
  for fl in files:
   size(fl)
 else:
  size(thing)

