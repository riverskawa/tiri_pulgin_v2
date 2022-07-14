
from tkinter import *
from PIL import Image, ImageTk
import cv2


root=Tk()

root.title("My Image")

w = Canvas(root,width=1000,height=1000)
ww= Canvas(root,width=1000,height=1000)

#--------------------left---------------------------------------
img_impt = cv2.imread('./temp_testing/20210908100212815C_0.bmp')
img_cv = cv2.cvtColor(img_impt, cv2.COLOR_BGR2RGBA)
c_img = Image.fromarray(img_cv)
img_TK = ImageTk.PhotoImage(image=c_img)
# image = Image.open()
w.create_image(0, 0, anchor=NW, image=img_TK)
#_-------------------------------------------------------------

#--------------------right---------------------------------------
img_impt2 = cv2.imread('./temp_testing/20210908100212815C_1.bmp')
img_cv2 = cv2.cvtColor(img_impt2, cv2.COLOR_BGR2RGBA)
c_img2 = Image.fromarray(img_cv2)
img_TK2 = ImageTk.PhotoImage(image=c_img2)
# image = Image.open()
ww.create_image(0, 0, anchor=NW, image=img_TK2)
#_-------------------------------------------------------------

w.grid(row=0,column=0,rowspan=1,columnspan=1)
ww.grid(row=0,column=1,rowspan=1,columnspan=1)

root.mainloop()