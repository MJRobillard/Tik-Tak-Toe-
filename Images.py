import tkinter
import tkinter as tk
from tkinter import ttk

map = [[" ", " ", " "], [" ", " ", " "], [' ', ' ', ' ']]
options = []
for k in range(len(map)):
    for s in range(len(map[k])):
        options.append([s, k])


def win(x, y, p):
    ready = True
    for x in range(3):
        if (map[x][0] is p) and (map[x][1] is p) and (
                map[x][2] is p) and (ready):  # check for same elemnet going  up from the og coordinates
            return (popupmsg("  " + p + ' won!!!!!'))
        if (map[0][x] is p) and (map[1][x] is p) and (
                map[2][x] is p) and (ready):  # check for same elemnet going  right from the og coordinates
            return popupmsg("  " + p + ' won!!!!!')
    if (map[0][0] is p) and (map[1][1] is p) and (
            map[2][2] is p) and (ready):  # check for same elemnet going diagonal down right  up from the og coordinates
        return (popupmsg("  " + p + ' won!!!!!'))
    if (map[2][0] is p) and (map[1][1] is p) and (map[0][2] is p) and (ready):  # diagonal down left
        return (popupmsg("  " + p + ' won!!!!!'))
    # check for same elemnet going  up from the og coordinates

    return (False)



master = tkinter.Tk()
master.title("grid() method")
master.geometry("350x275")
Text = " "
text = " "


def xplace00():
    global Text
    global map
    map[0][0] = 'x'
    Text = 'X'
    button00 = tkinter.Button(master, image=Xmage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=oplace00)
    button00.grid(row=0, column=0)
    if win(0, 0, 'x') != False:
        print(win(0, 0, 'x'))


def oplace00():
    global Text
    Text = 'O'
    global map
    map[0][0] = 'o'
    button00 = tkinter.Button(master, image=Omage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=xplace00)
    button00.grid(row=0, column=0)
    if win(0, 0, 'o') != False:
        print(win(0, 0, 'o'))


def xplace01():
    global Text
    Text = 'X'
    global map
    map[0][1] = 'x'
    button01 = tkinter.Button(master, image=Xmage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=oplace2)
    button01.grid(row=0, column=1)
    if win(0, 1, 'x') != False:
        print(win(0, 1, 'x'))


def oplace2():
    global Text
    Text = 'O'
    global map
    map[0][1] = 'o'
    button01 = tkinter.Button(master, image=Omage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=xplace01)
    button01.grid(row=0, column=1)
    if win(0, 1, 'o') != False:
        print(win(0, 1, 'o'))


def xplace02():
    global Text
    Text = 'X'
    global map
    map[0][2] = 'x'
    button02 = tkinter.Button(master, image=Xmage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=oplace3)
    button02.grid(row=0, column=2)
    if win(0, 2, 'x') != False:
        print(win(0, 2, 'x'))


def oplace3():
    global Text
    Text = 'O'
    global map
    map[0][2] = 'o'
    button = tkinter.Button(master, image=Omage, height=90, background="navy", width=80, font=("Ariel", 8),
                            activebackground="grey", command=xplace02)
    button.grid(row=0, column=2)

    if win(0, 2, 'o') != False:
        print(win(0, 2, 'o'))


def xplace10():
    global Text
    Text = 'X'
    global map
    map[1][0] = 'x'
    button10 = tkinter.Button(master, image=Xmage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=oplace4)
    button10.grid(row=1, column=0)
    if win(1, 0, 'x') != False:
        print(win(1, 0, 'x'))


def oplace4():
    global Text
    Text = 'O'
    global map
    map[1][0] = 'o'
    button10 = tkinter.Button(master, image=Omage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=xplace10)
    button10.grid(row=1, column=0)
    if win(1, 0, 'o') != False:
        print(win(1, 0, 'o'))


def xplace11():
    global Text
    Text = 'X'
    global map
    map[1][1] = 'x'
    button11 = tkinter.Button(master, image=Xmage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=oplace11)
    button11.grid(row=1, column=1)
    if win(1, 1, 'x') != False:
        print(win(1, 1, 'x'))


def oplace11():
    global Text
    Text = 'O'
    global map
    map[1][1] = 'o'
    button10 = tkinter.Button(master, image=Omage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=xplace11)
    button10.grid(row=1, column=1)
    if win(1, 1, 'o') != False:
        print(win(1, 1, 'o'))


def xplace12():
    global Text
    Text = 'X'
    global map
    map[1][2] = 'x'
    button12 = tkinter.Button(master, image=Xmage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=oplace12)
    button12.grid(row=1, column=2)
    if win(1, 2, 'x') != False:
        print(win(1, 2, 'x'))


def oplace12():
    global Text
    Text = 'O'
    global map
    map[1][2] = 'o'
    button12 = tkinter.Button(master, image=Omage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=xplace12)
    button12.grid(row=1, column=2)
    if win(1, 2, 'o') != False:
        print(win(1, 2, 'o'))


def xplace20():
    global Text
    Text = 'X'
    global map
    map[2][0] = 'x'
    button20 = tkinter.Button(master, image=Xmage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=oplace20)
    button20.grid(row=2, column=0)
    if win(2, 0, 'x') != False:
        print(win(2, 0, 'x'))


def oplace20():
    global Text
    Text = 'O'
    global map
    map[2][0] = 'o'
    button20 = tkinter.Button(master, image=Omage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=xplace20)
    button20.grid(row=2, column=0)
    if win(2, 0, 'o') != False:
        print(win(2, 0, 'o'))


def xplace21():
    global Text
    Text = 'X'
    global map
    map[2][1] = 'x'
    button21 = tkinter.Button(master, image=Xmage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=oplace21)
    button21.grid(row=2, column=1)
    if win(2, 1, 'x') != False:
        print(win(2, 1, 'x'))


def oplace21():
    global Text
    Text = 'O'
    global map
    map[2][1] = 'o'
    button21 = tkinter.Button(master, image=Omage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=xplace21)
    button21.grid(row=2, column=1)
    if win(2, 1, 'o') != False:
        print(win(2, 1, 'o'))


def xplace22():
    global Text
    Text = 'X'
    global map
    map[2][2] = 'x'
    button21 = tkinter.Button(master, image=Xmage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=oplace22)
    button21.grid(row=2, column=2)
    if win(2, 2, 'x') != False:
        print(win(2, 2, 'x'))


def oplace22():
    global Text
    Text = 'O'
    global map
    map[2][2] = 'o'
    button21 = tkinter.Button(master, image=Omage, height=90, background="navy", width=80, font=("Ariel", 8),
                              activebackground="grey", command=xplace22)
    button21.grid(row=2, column=2)
    if win(2, 2, 'o') != False:
        print(win(2, 2, 'o'))


Omage = tk.PhotoImage(file=r"C:\Users\ratth\PycharmProjects\Chess\Omage.PNG")
Xmage = tk.PhotoImage(file=r"C:\Users\ratth\PycharmProjects\Chess\Xmage.PNG")
mage = tk.PhotoImage(file=r"C:\Users\ratth\PycharmProjects\Chess\Blank.PNG")
button00 = tkinter.Button(master, image=mage, height=90, background="navy", width=80, font=("Ariel", 8),
                          activebackground="grey",
                          command=xplace00)
button00.grid(row=0, column=0)
button01 = tkinter.Button(master, image=mage, height=90, background="navy", width=80, font=("Ariel", 8),
                          activebackground="grey",
                          command=xplace01)
button01.grid(row=0, column=1)
button02 = tkinter.Button(master, image=mage, height=90, background="navy", width=80, command=xplace02,
                          font=("Ariel", 8),
                          activebackground="grey")
button02.grid(row=0, column=2)
button10 = tkinter.Button(master, image=mage, height=90, background="navy", width=80, command=xplace10,
                          font=("Ariel", 8),
                          activebackground="grey")
button10.grid(row=1, column=0)
button11 = tkinter.Button(master, image=mage, height=90, background="navy", width=80, command=xplace11,
                          font=("Ariel", 8),
                          activebackground="grey")
button11.grid(row=1, column=1)
button12 = tkinter.Button(master, image=mage, height=90, background="navy", width=80, command=xplace12,
                          font=("Ariel", 8),
                          activebackground="grey")
button12.grid(row=1, column=2)
button20 = tkinter.Button(master, image=mage, height=90, background="navy", width=80, command=xplace20,
                          font=("Ariel", 8),
                          activebackground="grey")
button20.grid(row=2, column=0)
button21 = tkinter.Button(master, image=mage, height=90, background="navy", width=80, command=xplace21,
                          font=("Ariel", 8),
                          activebackground="grey")
button21.grid(row=2, column=1)
button22 = tkinter.Button(master, image=mage, height=90, background="navy", width=80, command=xplace22,
                          font=("Ariel", 8),
                          activebackground="grey")
button22.grid(row=2, column=2)
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=LARGE_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


master.mainloop()
