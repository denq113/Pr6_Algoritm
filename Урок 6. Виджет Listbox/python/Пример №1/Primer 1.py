from tkinter import *
root = Tk()
lbox = Listbox(width=15, height=8)
lbox.pack()
for i in ('one', 'two', 'tree', 'four', 'five', 'six', 'seven'):
    lbox.insert(0, i)
root.mainloop()
