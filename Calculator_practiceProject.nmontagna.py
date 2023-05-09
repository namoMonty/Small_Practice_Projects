import tkinter as tk
import math


'''
                                                        ***SIMPLE CALCULATOR***
'''
# global Variables
txt_Height = 2    # height of txtbox
txt_Width  = 20   # with of txtbox

# font size
fontSize = 20


calculation = ""

# add new calculation
def addCalc(symbol):
    global calculation
    calculation += str(symbol)
    txtResult.delete(1.0,"end")
    txtResult.insert(1.0, calculation)

'''
evaluates function as string and removes end
and inserts the new calculation
'''
def evalCalc():
    global calculation
    try:
        # evaluate --> returns string
        calculation = str(eval(calculation))
        # update results
        txtResult.delete(1.0, "end")
        txtResult.insert(1.0, calculation)

    except:
        clear()
        txtResult.insert(1.0, "ERROR!")


def clear():
    txtResult.delete(1.0, "end")

# window
win = tk.Tk()
win.geometry("300x350")

# text
txtResult = tk.Text(win,height=txt_Height,width=txt_Width, font=("Arial", fontSize) )
txtResult.grid(columnspan=10)

'''
---------------------------------------Number_Buttons---------------------------------------------------------
'''
numButton_Width = 8  #buttonWidth global

#b1
numButton_1 = tk.Button(win,text="1",command= lambda: addCalc(1), width=numButton_Width,font=("Arial", 15))
numButton_1.grid(row=1, column=1)

#b2
numButton_2 = tk.Button(win,text="2",command= lambda: addCalc(2), width=numButton_Width,font=("Arial", 15))
numButton_2.grid(row=1, column=2)

#b3
numButton_3 = tk.Button(win,text="3",command= lambda: addCalc(3), width=numButton_Width,font=("Arial", 15))
numButton_3.grid(row=1, column=3)

#b4
numButton_4 = tk.Button(win,text="4",command= lambda: addCalc(4), width=numButton_Width,font=("Arial", 15))
numButton_4.grid(row=2, column=1)

#b5
numButton_5 = tk.Button(win,text="5",command= lambda: addCalc(5), width=numButton_Width,font=("Arial", 15))
numButton_5.grid(row=2, column=2)

#b6
numButton_6 = tk.Button(win,text="6",command= lambda: addCalc(6), width=numButton_Width,font=("Arial", 15))
numButton_6.grid(row=2, column=3)

#b7
numButton_7 = tk.Button(win,text="7",command= lambda: addCalc(7), width=numButton_Width,font=("Arial", 15))
numButton_7.grid(row=3, column=1)

#b8
numButton_8 = tk.Button(win,text="8",command= lambda: addCalc(8), width=numButton_Width,font=("Arial", 15))
numButton_8.grid(row=3, column=2)

#b9
numButton_9 = tk.Button(win,text="9",command= lambda: addCalc(9), width=numButton_Width,font=("Arial", 15))
numButton_9.grid(row=3, column=3)

#b0
numButton_0 = tk.Button(win,text="0",command= lambda: addCalc(0), width=numButton_Width,font=("Arial", 15))
numButton_0.grid(row=4, column=2)

'''
---------------------------------------Operators---------------------------------------------------------------
'''
# open | close

#open
openButton = tk.Button(win,text="(",command= lambda: addCalc("("), width=numButton_Width,font=("Arial", 15))    # L-bracket
openButton.grid(row=4, column=1)
# close
closeButton = tk.Button(win,text=")",command= lambda: addCalc(")"), width=numButton_Width,font=("Arial", 15))   # R-bracket
closeButton.grid(row=4, column=3)

# add | subtract

# Add
addButton = tk.Button(win,text="+",command= lambda: addCalc("+"), width=13,font=("Arial", 15))
addButton.grid(row=5, column=1,columnspan=2, sticky="ws")

# Subtract
subButton = tk.Button(win,text="-",command= lambda: addCalc("-"), width=13,font=("Arial", 15))
subButton.grid(row=5, column=2,columnspan=3,sticky="es")

# multiply | divide

# Divide
divButton = tk.Button(win,text="÷ ",command= lambda: addCalc("/"), width=13,font=("Arial", 15))
divButton.grid(row=6, column=1,columnspan=2, sticky="ws")

# Multiply
mulButton = tk.Button(win,text="x",command= lambda: addCalc("*"), width=13,font=("Arial", 15))
mulButton.grid(row=6, column=2,columnspan=3, sticky="es")

'''
---------------------------------------ALT-Operators----------------------------------------------------------
'''
# Enter (calulate input)
divButton = tk.Button(win,text="=",command= evalCalc, width=13,font=("Arial", 15))
divButton.grid(row=7, column=1,columnspan=2, sticky="ws")
# CLEAR
divButton = tk.Button(win,text="C",command= clear, width=13,font=("Arial", 15))
divButton.grid(row=7, column=2,columnspan=2, sticky="es")

win.mainloop()