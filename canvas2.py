#Version of canvas2 06/14/2017
#changes squares from previous versions into four Buttons 
#upon clicking any of the four buttons, a random color is chosen to become the button color (only works once)
#tone plays if red is the color that is randomly chosen to color the button
#writes the button name (example: square 1 for the square in the top left), the randomly chosen color of the button, 
#   and the date/time of the selection for the last button that was clicked to a canvas.db file

#Issues of this version: (1) randomly chooses color of square instead of user being able to use the keyboard to choose a color
#    (2) only works the first time the button is pressed i.e. the color doesn't change if you press the button a second time 
#    (3) only writes the button name, color, and date/time of the last button that is pressed i.e. it overwrites previous selections

#Benefits of this version: (1) User selects the square they want to change the color of by clicking the button with the mouse 

import os, sys
import time
from Tkinter import *
import random
import winsound

master=Tk()

#function that governs the button in the top left (square 1)
#when the square 1 button is clicked, the button color changes to a color randomly selected from a list
#tone plays if red is randomly chosen 
#writes square 1, color name, and date time if square 1 is the last button that is clicked  
def square1():
    color = ["red", "orange", "yellow", "green", "blue", "violet"]
    c1 = random.choice(color)
    button1 = Button(text = "square 1", bg = c1)
    button1.configure(width = 10, height = 5, activebackground = "#D2D2D2", relief = GROOVE)
    button1_window = canvas.create_window(10, 10, anchor=NW, window=button1)
    button1.update()
    if c1 == "red":
        winsound.Beep(275,1000)
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    f = open(filename, 'w')
    f.write("square 1 " + c1 + " " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    f.close()

#function that governs the button in the bottom left (square 2)
#when the the square 2 button is clicked, the button color changes to a random color selected from a list 
#tone plays if red is randomly chosen 
#writes square 2, color name, and date time if square 2 is the last button that is clicked 
def square2():
    color = ["red", "orange", "yellow", "green", "blue", "violet"]
    c2 = random.choice(color)
    button2 = Button(text = "square 2", bg = c2)
    button2.configure(width = 10, height = 5, activebackground = "#D2D2D2", relief = GROOVE)
    button2_window = canvas.create_window(10, 100, anchor=NW, window=button2)
    button2.update()
    if c2 == "red":
        winsound.Beep(275,1000)
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    f = open(filename, 'w')
    f.write("square 2 " + c2 + " " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    f.close()

#function that governs the button in the top right (button 3)
#when the square 3 button is clicked, the button color changes to a color randomly selected from a list 
#tone plays if red is randomly chosen 
#writes square 3, color name, and date time if square 3 is the last button that is clicked 
def square3():
    color = ["red", "orange", "yellow", "green", "blue", "violet"]
    c3 = random.choice(color)
    button3 = Button(text = "square 3", bg = c3)
    button3.configure(width = 10, height = 5, activebackground = "#D2D2D2", relief = GROOVE)
    button3_window = canvas.create_window(100, 10, anchor=NW, window=button3)
    button3.update()
    if c3 == "red":
        winsound.Beep(275,1000)
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    f = open(filename, 'w')
    f.write("square 3 " + c3 + " " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    f.close()

#function that governs the button in the bottom right (button 4)
#when the square 4 button is clicked, the button color changes to a color randomly selected from a list 
#tone plays if red is randomly chosen 
#writes square 4, color name, and date time if square 4 is the last button that is clicked 
def square4():
    color = ["red", "orange", "yellow", "green", "blue", "violet"]
    c4 = random.choice(color)
    button4 = Button(text = "square 4", bg = c4)
    button4.configure(width = 10, height = 5, activebackground = "#D2D2D2", relief = GROOVE)
    button4_window = canvas.create_window(100, 100, anchor=NW, window=button4)
    button4.update()
    if c4 == "red":
        winsound.Beep(275,1000)
    filename = "C:\\Users\\Olivia\\Desktop\\DUNE\\Python\\canvas.db"
    dirname = os.path.dirname(filename)
    if not os.path.exists(dirname):
        os.makedirs(dirname, 755)
    f = open(filename, 'w')
    f.write("square 4 " + c4 + " " + str(time.strftime("%Y/%m/%d %H:%M:%S")))
    f.close()

#draws canvas for the buttons to appear on    
canvas = Canvas(master, height = 200, width = 200)
canvas.pack()

#square 1 is the button in the top left corner 
button1 = Button(text = "square 1", command=square1)
button1.configure(width = 10, height = 5, activebackground = "white", relief = GROOVE) #height and width are tricky (button is a square but height and width are different)
button1_window = canvas.create_window(10, 10, anchor=NW, window=button1)
button1.update()

#square 2 is the button in the bottom left 
button2 = Button(text = "square 2", command = square2)
button2.configure(width = 10, height = 5, activebackground = "white", relief = GROOVE)
button2_window = canvas.create_window(10, 100, anchor=NW, window=button2)
button2.update()

#square 3 is the button in the top right 
button3 = Button(text = "square 3", command = square3)
button3.configure(width = 10, height = 5, activebackground = "white", relief = GROOVE)
button3_window = canvas.create_window(100, 10, anchor=NW, window=button3)
button3.update()

#square 4 is the button in the bottom right
button4 = Button(text = "square 4", command = square4)
button4.configure(width = 10, height = 5, activebackground = "white", relief = GROOVE)
button4_window = canvas.create_window(100, 100, anchor=NW, window=button4)
button4.update()

master.mainloop()
