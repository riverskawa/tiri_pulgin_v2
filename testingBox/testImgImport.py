from tkinter import *
from PIL import Image, ImageTk

root=Tk()

root.title("My Image")

w = Canvas(root, width=50, height=250)

image = Image.open('./demo2.png')
w.create_image((0, 0),image=ImageTk.PhotoImage(image))

w.pack()

root.mainloop()