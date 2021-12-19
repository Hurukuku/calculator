from tkinter import *
import os, sys
import tkinter.font as font 
expression = ""
def gui():
    global output
    window = Tk()
    window.geometry("223x331")
    calcfont = font.Font(size = 15)
    output = StringVar()
    window.title("Calculator")
    window.iconbitmap(resource_path("icon.ico"))
    window.configure(background="black")
    outputfield = Entry(window,font=calcfont, textvariable=output, bg = "black", fg = "white") .grid(column = 0,row = 0, columnspan=4, sticky=W, ipady=5)
    button1 = Button(window, text = ' 1 ', bg = "black", fg = "white",font=calcfont ,command = lambda: numpress(1), width= 4, height=2  ) .grid(row = 1, column = 0 )
    button2 = Button(window, text = ' 2 ', bg = "black", fg = "white",font=calcfont ,command = lambda: numpress(2), width= 4, height=2  ) .grid(row = 1, column = 1 )
    button3 = Button(window, text = ' 3 ', bg = "black", fg = "white",font=calcfont ,command = lambda: numpress(3), width= 4, height=2  ) .grid(row = 1, column = 2 )
    button4 = Button(window, text = ' 4 ', bg = "black", fg = "white",font=calcfont ,command = lambda: numpress(4), width= 4, height=2  ) .grid(row = 2, column = 0 )
    button5 = Button(window, text = ' 5 ', bg = "black", fg = "white",font=calcfont ,command = lambda: numpress(5), width= 4, height=2  ) .grid(row = 2, column = 1 )
    button6 = Button(window, text = ' 6 ', bg = "black", fg = "white",font=calcfont ,command = lambda: numpress(6), width= 4, height=2  ) .grid(row = 2, column = 2 )
    button7 = Button(window, text = ' 7 ', bg = "black", fg = "white",font=calcfont ,command = lambda: numpress(7), width= 4, height=2  ) .grid(row = 3, column = 0 )
    button8 = Button(window, text = ' 8 ', bg = "black", fg = "white",font=calcfont ,command = lambda: numpress(8), width= 4, height=2  ) .grid(row = 3, column = 1 )
    button9 = Button(window, text = ' 9 ', bg = "black", fg = "white",font=calcfont ,command = lambda: numpress(9), width= 4, height=2  ) .grid(row = 3, column = 2 )
    button0 = Button(window, text = ' 0 ', bg = "black", fg = "white",font=calcfont ,command = lambda: numpress(0), width= 4, height=2  ) .grid(row = 4, column = 1 )
    decimalbutton = Button(window, text = ' . ', bg = "black", fg = "white",font=calcfont,command = lambda: numpress('.'), width= 4, height=2 ) .grid(row = 4, column = 0 )
    addbutton = Button(window, text = ' + ', bg = "black", fg = "white",font=calcfont, command = lambda: numpress(' + '), width=4, height=2 ) .grid(row = 4, column = 3 )
    substractbutton = Button(window, text = ' - ', bg = "black", fg = "white",font=calcfont, command = lambda: numpress(' - '), width=4, height=2 ) .grid(row = 1, column = 3 )
    dividebutton = Button(window, text = ' / ', bg = "black", fg = "white",font=calcfont, command = lambda: numpress(' / '), width=4, height=2) .grid(row = 2, column = 3 )
    multiplybutton = Button(window, text = ' * ', bg = "black", fg = "white",font=calcfont, command = lambda: numpress(' * '), width=4, height=2) .grid(row = 3, column = 3 )
    equalsbutton = Button(window, text = ' = ', bg = "black", fg = "white",font=calcfont, command = lambda: equals(), width = 4, height=2) .grid (row = 4, column = 2)
    clearbutton = Button(window, text = ' C ', bg = "black", fg = "white",font=calcfont, command = lambda: clear(), width = 4, height=1) .grid (row = 5, column = 0)
    binarybutton = Button(window, text = ' bin ', bg = "black", fg = "white",font=calcfont, command = lambda: nums(2), width = 4, height=1) .grid (row = 5, column = 1)
    hexbutton = Button(window, text = 'hex', bg = "black", fg = "white",font=calcfont, command = lambda: nums(16), width = 4, height=1) .grid (row = 5, column = 2)
    octbutton = Button(window, text = 'oct', bg = "black", fg = "white",font=calcfont, command = lambda: nums(8), width = 4, height=1) .grid (row = 5, column = 3)
    window.mainloop()
def nums(fun):
    global expression
    if expression != "":
        if fun == 2:
            total = ''.join([i for i in bin(int(expression))[2:]])
        if fun == 16:
            total = ''.join([i for i in hex(int(expression))[2:]])
        if fun == 8:
            total = ''.join([i for i in oct(int(expression))[2:]])
        expression = ""
        output.set(total)
def numpress(num): 
    global expression
    expression = expression + str(num)
    output.set(expression)   
def equals():
    global expression
    if expression != "":
        try:
            total = str(eval(expression))
            output.set(total)
            expression = str(total)
        except Exception as e :
            output.set(f"{e}")
            expression = ""
    else: clear()
def clear():
    global expression
    expression = ""
    output.set("")
def resource_path(relative_path): # icon in pyinstaller
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)   
if __name__ == "__main__":
    gui() 
