from time import sleep as sl

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

talking=True

conv=""

def sp(text):
 global conv
 conv+="[Client] "+text+"\n"

def spe(text):
 global conv
 print(text)
 conv+=text
 conv+="\n"

f=open("burbs.txt","r")
for line in f:
 print(line,end="")
 conv+=line
f.close()

spe("[Info] Client Player is no longer AFK.")
while talking:
 txt=input("[Client] ")
 sl(0.5)
 if(txt=="detach"):
  spe("[Info] Client Player is now AFK.")
  print("\n\nCall the file \"attach_to_chat.py\" to reattach.")
  talking=False
  f=open("burbs.txt","w")
  f.write(conv)
  f.close()
 else: 
  sp(txt)
