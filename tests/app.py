from tkinter import *
root = Tk()
root.iconbitmap("icon.ico")
label = Label(root,text=open('assets/text.txt','rb').read())
label.pack()
root.mainloop()