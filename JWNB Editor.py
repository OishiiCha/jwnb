import tkinter as tk
from tkinter import *

root=Tk("JWNB Editor")
root.config(bg='grey12')
root.geometry('1000x400')
root.resizable(width=False, height=False)

f = open('data.jwnb')
f1 = f.read()
f.close()

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    file1=open('data.jwnb', "w+")
    file1.write(t)
    file1.close()


myfont = ('arial',20)

xscroll = Scrollbar(root,orient=HORIZONTAL,elementborderwidth=-1,width=30)
xscroll.pack(side=BOTTOM,fill=BOTH)
button=Button(root, text="Save", bg='grey26',fg='white', font=myfont, command=saveas) 
button.pack(expand=1)


text=Text(root,height='600', xscrollcommand=xscroll.set, wrap=NONE, width='1500',padx=10,pady=10, bg='grey12',fg='white',insertbackground='white', font=myfont,state="normal",relief=GROOVE)
xscroll.config(command=text.xview)
text.pack(fill=BOTH,expand=1)

text.insert(tk.END,f1)
root.mainloop()