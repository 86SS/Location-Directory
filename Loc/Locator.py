#===========================================================================================TREE AND SHRUB LOCATOR======================================================================================
'''                                                                                     LUCAS ZLOCK    12/13/2016    5.0                                                                             '''
'''
UPDATES (SEPARATED BY COMMAS): 12/13/2016, 12/13/2016, 12/15/2016, 12/18/2016, 12/30/2016
'''
#===========================================================================================TREE AND SHRUB LOCATOR======================================================================================
''' 
***EDITORS NOTE***
Perhaps prices can be added in the future as well. With a buttom maybe?
A new CSV would be needed.

Perhaps make an executable from this.

This code can be easily edited to perform as an animated directory for perhaps a shopping mall, or parking garage, etc.
'''
#================================================================================================DO NOT ALTER CODE======================================================================================
#================================================================================================DO NOT ALTER CODE======================================================================================
#================================================================================================DO NOT ALTER CODE======================================================================================

import csv
import collections
from tkinter import *
import turtle
wn = turtle.Screen() #sets up window
wn.setup (width=.5, height=1.0, startx=-1, starty=0) #sets to 50% by 100%, top right of screen
turtle.bgpic("WilleysMap.gif") #loads picture of map

def direction(n):
    m = turtle.Turtle() #creates arrow
    m.speed(100) #sets the speed
    m.penup() #lifts pen so no marks are made
    m.forward(160)
    m.right(90)
    m.forward(80)
    m.speed(1) #reduces speed so path can be seen
    if n == 1:#------------------------------------------------------------------NU 1
        m.pencolor("red")
        m.pensize(15)
        m.pendown()
        m.forward(20)
        m.right(90)
        m.forward(180)
        m.right(90)
        m.forward(300)
        m.left(90)
        m.forward(80)
        wn.mainloop()       
    elif n == 2: #---------------------------------------------------------------NU 2
        m.pencolor("red")
        m.pensize(15)
        m.pendown()
        m.forward(20)
        m.right(90)
        m.forward(180)
        m.right(90)
        m.forward(235)
        m.left(90)
        m.forward(80)
        wn.mainloop()       
    elif n == 3: #---------------------------------------------------------------NU 3
        m.pencolor("red")
        m.pensize(15)
        m.pendown()
        m.forward(20)
        m.right(90)
        m.forward(180)
        m.right(90)
        m.forward(180)
        m.left(90)
        m.forward(80)
        wn.mainloop()
    elif n == 4: #---------------------------------------------------------------NU 4
        m.pencolor("red")
        m.pensize(15)
        m.pendown()
        m.forward(20)
        m.right(90)
        m.forward(180)
        m.right(90)
        m.forward(300)
        m.right(90)
        m.forward(80)
        wn.mainloop()
    elif n == 5: #---------------------------------------------------------------NU 5
        m.pencolor("red")
        m.pensize(15)
        m.pendown()
        m.forward(20)
        m.right(90)
        m.forward(180)
        m.right(90)
        m.forward(200)
        m.right(90)
        m.forward(80)
        wn.mainloop()       
    elif n == 6: #---------------------------------------------------------------NU DECK
        m.pencolor("red")
        m.pensize(15)
        m.pendown()
        m.forward(20)
        m.right(90)
        m.forward(180)
        m.right(90)
        m.forward(60)
        m.left(90)
        m.forward(80)
        wn.mainloop()
    elif n == 7: #---------------------------------------------------------------PARKING LOT
        m.pencolor("red")
        m.pensize(15)
        m.pendown()
        m.forward(20)
        m.left(90)
        m.forward(50)
        m.left(45)
        m.forward(140)
        m.left(45)
        m.forward(100)
        m.left(45)
        m.forward(180)
        wn.mainloop()
    elif n == 8: #---------------------------------------------------------------HUT AREA
        m.pencolor("red")
        m.pensize(15)
        m.pendown()
        m.forward(20)
        m.right(90)
        m.forward(80)
        m.right(90)
        m.forward(40)
        wn.mainloop()
    elif n == 9: #---------------------------------------------------------------SIDE STRUCTURE 1
        m.pencolor("red")
        m.pensize(15)
        m.pendown()
        m.forward(20)
        m.right(90)
        m.forward(180)
        m.left(90)
        m.forward(30)
        m.right(90)
        m.forward(80)
        wn.mainloop()
    else: #----------------------------------------------------------------------SIDE STRUCTURE 2
        m.pencolor("red")
        m.pensize(15)
        m.pendown()
        m.forward(80)
        m.right(90)
        m.forward(60)
        wn.mainloop()
    

with open('code.csv') as f: #loads itemDict from the code.csv file
    reader1 = csv.reader(f)
    itemDict = dict(reader1)

with open('loc.csv') as f: #loads itemLoc from the loc.csv file
    reader2 = csv.reader(f)
    itemLoc = dict(reader2)
itemLoc['Emerald Green Arborvitae'] = itemLoc.pop('﻿Emerald Green Arborvitae') #corrects error in translation

global find
def evaluate(event):
    if entry.get() in itemDict:
        res.configure(text = "UPC: " + str(entry.get()) + "\n The " + itemDict[entry.get()] + " can be found at: " + itemLoc[itemDict[entry.get()]], font = "Verdana 15 bold")
    else:
        res.configure(text = "UPC: " + str(entry.get()) + "\n The UPC you entered is not listed", font = "Verdana 15 bold")
        
def show():
    turtle.clearscreen()    
    turtle.bgpic("WilleysMap.gif") #loads picture of map    
    if itemLoc[itemDict[entry.get()]] == 'NU 1':
        direction(1)
    elif itemLoc[itemDict[entry.get()]] == 'NU 2':
        direction(2)
    elif itemLoc[itemDict[entry.get()]] == 'NU 3':
        direction(3)    
    elif itemLoc[itemDict[entry.get()]] == 'NU 4':
        direction(4)
    elif itemLoc[itemDict[entry.get()]] == 'NU 5':
        direction(5)
    elif itemLoc[itemDict[entry.get()]] == 'NU DECK':
        direction(6)    
    elif itemLoc[itemDict[entry.get()]] == 'PARKING LOT':
        direction(7)    
    elif itemLoc[itemDict[entry.get()]] == 'HUT AREA':
        direction(8)
    elif itemLoc[itemDict[entry.get()]] == 'SIDE STRUCTURE 1':
        direction(9)    
    else:
        direction(10)
   
w = Tk()

width, height = w.winfo_screenwidth(), w.winfo_screenheight()
width = width/2.05
w.geometry('%dx%d+0+0' % (width,height))

Label(w, text="TREE AND SHRUB LOCATOR", font = "Verdana 10").pack()
Label(w, text="LUCAS ZLOCK    12/13/2016    version 4.0", font = "Verdana 10").pack()
Label(w, text="").pack()

Label(w, text="INSTRUCTIONS:", font = "Verdana 12 bold").pack(anchor=W)
Label(w, text="To add inventory, go to code.csv file. Location of new inventory must be updated in loc.csv", font = "Verdana 10 bold").pack(anchor=W)
Label(w, text="file. Stock.xlsx is the master sheet. It must be updated as well. Enter the desired UPC in the ", font = "Verdana 10 bold").pack(anchor=W)
Label(w, text="entry box and press 'Enter'. If an invalid UPC is entered, an error message will be displayed.", font = "Verdana 10 bold").pack(anchor=W)
Label(w, text="To find the location of a different item, simply type the new UPC in the entry box and press", font = "Verdana 10 bold").pack(anchor=W)
Label(w, text="'Enter' again. To see a visual representation of the items location, press the 'Show' button.", font = "Verdana 10 bold").pack(anchor=W)
Label(w, text="").pack()

Label(w, text="Please enter UPC of item", font = "Verdana 10 bold").pack()
Label(w, text="you would like to locate", font = "Verdana 10 bold").pack()
Label(w, text="and press 'Enter'", font = "Verdana 10 bold").pack()
entry = Entry(w)
entry.focus_set()

entry.bind("<Return>", evaluate)
entry.pack()

Label(w, text="").pack()

Button(w, text ="Show",font = "Verdana 10 bold", bd = 5, command=show).pack()

Label(w, text="").pack()

res = Label(w)
res.pack()

Label(w, text="Scroll down to see all listed UPCs", font = "Verdana 10 bold").pack()

scrollbar = Scrollbar(w)
scrollbar.pack(side=RIGHT, fill=Y)
T = Text(w, height=18, width=78, bg = 'blue', fg = 'white', font = "Verdana 10 bold")
T.pack()
quote = ''
with open('code.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        quote += ("" + row[0] + '.'*(20-len(row[0])) + row[1] + '\n')
T.insert(END, quote)
scrollbar.config(command=T.yview)

w.mainloop()
