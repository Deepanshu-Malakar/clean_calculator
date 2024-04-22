import pywinstyles
from tkinter import *
from customtkinter import *
from PIL import Image
import pywinstyles

root=CTk(fg_color="white")
root.title("My Calculator")
set_appearance_mode("light")
set_default_color_theme("dark-blue")
pywinstyles.change_header_color(root,"#2156A6")
root.geometry("320x320")

f=CTkFrame(root,fg_color="transparent")
f.pack(side=TOP,padx=10,pady=10)
e=CTkEntry(f,width=300,justify="center",corner_radius=2,height=50,border_color="#303336",border_width=1,font=("calibri",20))
e.pack(padx=10,pady=10)

button_frame=CTkFrame(root,width=300,corner_radius=2)
button_frame.pack(pady=0,padx=20)

bfl=CTkFrame(button_frame,corner_radius=2,fg_color="white")
bfl.grid(row=0,column=0,padx=0,pady=0)

bfr=CTkFrame(button_frame,corner_radius=2,fg_color="white")
bfr.grid(row=0,column=1,padx=0,pady=0)

w=40
class Key:
    def __init__(self,r,c,t,color="transparent") -> None:
        self.text=t
        self.button=CTkButton(bfl,text=t,fg_color=color,text_color="black",command=self.click,width=70,height=w,corner_radius=2)
        self.button.grid(row=r,column=c,padx=0,pady=0) 
    def click(self):
        e.insert(END,self.text)
    def opacity(self,x):
        pywinstyles.set_opacity(self.button,x)

b7=Key(0,0,"7")        
b8=Key(0,1,"8")        
b9=Key(0,2,"9")
b4=Key(1,0,"4")        
b5=Key(1,1,"5")        
b6=Key(1,2,"6")
b1=Key(2,0,"1")        
b2=Key(2,1,"2")        
b3=Key(2,2,"3")
b_open=Key(3,0,"(")        
b_0=Key(3,1,"0")        
b_close=Key(3,2,")")
b_dot=Key(4,1,".")
def clear():
    # x=eval(e.get())
    e.delete(0,END)
    # e.insert(0,x)

b_clear=CTkButton(bfl,text="AC",fg_color="transparent",text_color="black",command=clear,width=70,height=w,corner_radius=2)
b_clear.grid(row=4,column=0,padx=0,pady=0)
def backspace():
    # x=eval(e.get())
    e.delete(len(e.get())-1)
    # e.insert(0,x)
i=CTkImage(Image.open(r"images\backspace.png"),size=(20,20))
b_back=CTkButton(bfl,text="",image=i,fg_color="transparent",text_color="black",command=backspace,width=70,height=w,corner_radius=2)
b_back.grid(row=4,column=2,padx=0,pady=0)

class Key2:
    def __init__(self,r,c,t,color="transparent") -> None:
        self.text=t
        self.button=CTkButton(bfr,text=t,fg_color="#8DA1C0",text_color="#2156A6",command=self.click,width=70,height=w,corner_radius=0)
        self.button.grid(row=r,column=c,padx=0,pady=0) 
    def click(self):
        e.insert(END,self.text)
    # def opacity(self,x):
        # pywinstyles.set_opacity(self.button,x)

minus=Key2(0,0,"-") 
plus=Key2(1,0,"+")
product=Key2(2,0,"*")
quotient=Key2(3,0,"/")
def equal():
    x=eval(e.get())
    e.delete(0,END)
    e.insert(0,x)
b_equal=CTkButton(bfr,text="=",fg_color="#2156A6",text_color="white",command=equal,width=70,height=w,corner_radius=2)
b_equal.grid(row=4,column=0,padx=0,pady=0)
root.mainloop()