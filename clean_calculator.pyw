import pywinstyles
from tkinter import *
from customtkinter import *
from PIL import Image

root=CTk(fg_color="white")
root.title("My Calculator")
set_appearance_mode("light")
set_default_color_theme("green")

root.geometry("320x320")

f=CTkFrame(root,fg_color="transparent")
f.pack(side=TOP,padx=10,pady=10)
e=CTkEntry(f,width=300,justify="center",corner_radius=2,height=50,border_color="#303336",border_width=1,font=("calibri",20))
e.pack(padx=10,pady=10)


root.mainloop()