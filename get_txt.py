# GUF with python
from tkinter import * 
root =Tk()
#Create text field space

e1=Entry(root,width=50 ,bg = "black",fg = "grey")

e1.pack()
e1.insert(0,"Enter your name")
#Second input


#Create a task function
def myclick():
    f_num=float (e1.pack)()
    s_num=float (e1.pack)()
    sub = f_num+s_num
    mult = f_num+s_num
    sum = f_num+s_num


    Ans ="Adittion"+str(add) + "subtraction" +str(add) +"multiplication"
    
    
    Hello="Hello ",e.pack
    my_Label =Label(root,text,e.pack)
    my_Label.pack()
# Create frame
myButton = Button (root,text="calculator", command =myclick)
myButton.pack ()

root.mainloop()