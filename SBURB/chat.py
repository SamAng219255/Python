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

print("SBURB Client connected and loaded. A chat window will now be opened with your server player. Type \"detach\" to detach.")
sl(3)
spe("[Server] Hello! Sorry gtg for a sec and do something.")
sl(1)
spe("[Info] Server Player is now AFK.")
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
