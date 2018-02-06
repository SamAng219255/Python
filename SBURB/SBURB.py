from tkinter import *
#import imageio

import simpleaudio as sa
import wave
import cv2
from PIL import Image, ImageTk

loadingScreen=0
timePassed=0
screenPhase=0
turn=0
wave_file = wave.open("SBURB.wav","rb")
wave_obj = sa.WaveObject.from_wave_read(wave_file)
count=0
jump=25

root=Tk()
root.title("SBURB")

newFiles=[PhotoImage(file="SBURBTerminal.gif",format="gif -index 1"),PhotoImage(file="SBURBTerminal.gif",format="gif -index 2"),PhotoImage(file="SBURBTerminal.gif",format="gif -index 3"),PhotoImage(file="SBURBTerminal.gif",format="gif -index 4"),PhotoImage(file="SBURBTerminal.gif",format="gif -index 5")]

root.geometry("1000x611")

cap=cv2.VideoCapture("SBURBLoading.mp4")
_, frame = cap.read()

def displayVid():
 global root
 global label
 global frame
 ret, frame = cap.read()
 if ret:
  frame = cv2.resize(frame, (0,0), fx=0.78125, fy=0.84861111)
  cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
  img = Image.fromarray(cv2image)
  imgtk = ImageTk.PhotoImage(image=img)
  label.imgtk = imgtk
  label.configure(image=imgtk)
  label.after(17, displayVid)
 else:
  root.destroy()
def keydown(e):
 global label
 global wave_obj
 global loadingScreen
 loadingScreen=1
 play_obj=wave_obj.play()
 label.lift()
 displayVid()
def displayImages():
 global loadingScreen
 global timePassed
 global screenPhase
 global canvas
 global turn
 if(not loadingScreen):
  timePassed+=1
  if(timePassed==33 and screenPhase==0):
   canvas.create_image(0,0,anchor="nw",image=newFiles[0])
   #print("round 1")
  elif(timePassed==49 and screenPhase==0):
   canvas.create_image(0,0,anchor="nw",image=newFiles[1])
   timePassed=0
   screenPhase=1
   #print("round 2")
  elif(turn==0 and timePassed==50 and screenPhase==1):
   canvas.create_image(0,0,anchor="nw",image=newFiles[2])
   timePassed=0
   turn=1
   #print("round 3")
  elif(turn==1 and timePassed==50 and screenPhase==1):
   canvas.create_image(0,0,anchor="nw",image=newFiles[3])
   timePassed=0
   turn=0
   #print("round 4")
  root.after(10,displayImages)

label=Label(root,width=1000,height=611)
canvas=Canvas(root,width=1000,height=611,bg="blue")
filename=PhotoImage(file="SBURBTerminal.gif",format="gif -index 0")
image=canvas.create_image(0,0,anchor="nw",image=filename)
root.bind("<KeyPress>", keydown)
canvas.place(height=611,width=1000,x=0,y=0)
label.place(height=611,width=1000,x=0,y=0)
canvas.focus_set()
root.after(10,displayImages)
root.mainloop()

import chat
