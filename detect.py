from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import cv2
import numpy as np
thumbstack_cascade = cv2.CascadeClassifier("cascade.xml")
root= Tk()
root.title("Thumbstack Logo detection using python")
root.geometry('500x500')

def openfileselectionbox():
    filepath= filedialog.askopenfilename(title="Select an Image file", filetypes=(("PNG files" ,"*.png"),("JPG files","*.jpg")))
    img= cv2.imread("C:/Users/Pia/Documents/Logo Detetion/2.png")
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    logo = thumbstack_cascade.detectMultiScale(gray,1.11,5)
    for(x,y,w,h) in logo:
        img= cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)


    cv2.imshow("Logos", img)
    cv2.waitKey(0)
    # messagebox.showinfo("showinfo", filepath)
  

def opencameradetector():
    vid = cv2.VideoCapture(0)
    while(True):
        ret, frame = vid.read()
        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        logo = thumbstack_cascade.detectMultiScale(gray,1.11,5)
        for(x,y,w,h) in logo:
            frame= cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)






        cv2.imshow('frame', frame)
        key = cv2.waitKey(10) 
        
        if cv2.getWindowProperty("frame", cv2.WND_PROP_VISIBLE) <1:
            break
    vid.release()
    cv2.destroyAllWindows()

button = Button(root, text = 'Detect Logo by Image file',command=openfileselectionbox)
button.pack(side = TOP, pady = 5)


button2 = Button(root, text = 'Detect Logo by camera',command=opencameradetector)
button2.pack(side = TOP, pady = 5)

root.mainloop()