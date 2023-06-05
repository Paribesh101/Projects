from tkinter import *
from tkinter import filedialog

#def openFile():
 #   filepath = filedialog.askopenfilename()
 #   file = open(filepath, 'r')
 #   print(file.read())
 #   file.close()

#window = Tk()
#button = Button(text="Open",command=openFile)
#button.pack()
#window.mainloop()

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return

    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()

#menu-bar

from tkinter import *

def openFile():
    print("File has been opened!")
def saveFile():
    print("File has been saved!")

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)

window.mainloop()

# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

Button(window,text="W",font=("Consolas",25),width=3).pack()
Button(window,text="A",font=("Consolas",25),width=3).pack()
Button(window,text="S",font=("Consolas",25),width=3).pack()
Button(window,text="D",font=("Consolas",25),width=3).pack()

window.mainloop()

from tkinter import *
from tkinter .ttk import *
import time

window = Tk()






window.mainloop()



