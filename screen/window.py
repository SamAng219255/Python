from tkinter import *

root=Tk()

frame=Frame(root,width=1024,height=512)
frame.pack()
controlFrame=Frame(frame,bg="black",width=256,height=512)
controlFrame.pack(side="right",expand=0)
viewFrame=Frame(frame,bg="blue",width=768,height=512)
viewFrame.pack(side="left",expand=0)

C=Canvas(viewFrame,bg="blue",width=768,height=512)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")
C.pack()

Label(controlFrame, text='Hello').pack()

root.title("Hello, World.")
root.mainloop()
