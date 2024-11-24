from tkinter import *

def MoveLeft():
    selected_items = box1.curselection()
    for i in selected_items:
        item = box1.get(i)
        box2.insert(END, item)
    for i in reversed(selected_items):
        box1.delete(i)

def MoveRight():
    selected_items = box2.curselection()
    for i in selected_items:
        item = box2.get(i)
        box1.insert(END, item)
    for i in reversed(selected_items):
        box2.delete(i)


root = Tk()

f1 = Frame()
f2 = Frame()
f3 = Frame()

box1 = Listbox(f1,selectmode=EXTENDED)
box2 = Listbox(f3,selectmode=EXTENDED)
b1 = Button(f2,text = ">>>", command= MoveLeft)
b2 = Button(f2,text = "<<<", command= MoveRight)

for i in ('Baklazan','Kapusta','Ogurez','Moloko','Slivki','Pomidorki','Chai','Voda','Makarony'):
    box1.insert(0, i)

box1.pack()
box2.pack()
b1.pack()
b2.pack()

f1.pack(side = LEFT)
f2.pack(side = LEFT)
f3.pack(side = LEFT)


root.mainloop()