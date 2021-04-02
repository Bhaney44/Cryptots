#Smart Contracts

##MIT License
#Copyright Brian Haney 2021
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import csv
from tkinter import *
import tkinter.messagebox as box

master = Tk()

#Parties
label0 = Label(master, text = 'Sender Address', relief = 'groove', width = 40)
label1 = Label(master, text = 'Receiver Address', relief = 'groove', width = 40)
Party_A = Entry(master, relief = 'groove', width = 40)
Party_B = Entry(master, relief = 'groove', width = 40)

#Tokens
label2 = Label(master, text = 'Algo', relief = 'groove', width = 40)
Tokens = Entry(master, relief = 'groove', width = 40)

#Signed
label3 = Label(master, text = 'Signature', relief = 'groove', width = 40)
label4 = Label(master, text = 'Transaction Number', relief = 'groove', width = 40)
Party_A_Sign = Entry(master, relief = 'groove', width = 40)
Party_B_Sign = Entry(master, relief = 'groove', width = 40)

#Date
label5 = Label(master, text = 'Date', relief = 'groove', width = 40)
Date = Entry(master, relief = 'groove', width = 40)


#write to file function
def write():
    
    #Define Variavles
    Party_Red = str(Party_A.get())
    Party_Blue = str(Party_B.get())
    Party_Red_C = str(Tokens.get())
    Party_Red_Sign = str(Party_A_Sign.get())
    Party_Blue_Sign = str(Party_B_Sign.get())
    Date_0 = str(Date.get())

    #Openfile
    with open('Algo.csv', 'a') as csvfile:
    #define fieldnames
        fieldnames = ['Sender', 'Tokens', 'Party A Signiture', 'Party B', 'Party B Signiture', 'Date']
    #define writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #Write
        writer.writerow({'Sender': Party_Red, 'Tokens':Party_Red_C, 'Party A Signiture':Party_Red_Sign,
                         'Party B': Party_Blue, 'Party B Signiture':Party_Blue_Sign,'Date': Date_0})

#Button to run write
b1 = Button(master, text = 'Execute Smart Contract', relief = 'groove', width = 25, command=write)

#function two to clear the entry widgets
def clear():
    Party_A.delete(0, END)
    Party_B.delete(0, END)
    Tokens.delete(0, END)
    Party_A_Sign.delete(0, END)
    Party_B_Sign.delete(0, END)
    Date.delete(0,END)
                        
#button to run function clear
b2 = Button(master, text = 'New Contract', relief = 'groove', width = 25, command=clear)

#Geometry
label0.grid( row = 1, column = 1, padx = 10 )
Party_A.grid( row = 2, column = 1, padx = 10 )
label1.grid( row = 1, column = 2, padx = 10 )
Party_B.grid( row = 2, column = 2, padx = 10 )

#Tokens
label2.grid( row = 3, column = 1, padx = 10 )
Tokens.grid( row = 3, column = 2, padx = 10 )

#Signed
label3.grid( row = 4, column = 1, padx = 10 )
label4.grid( row = 4, column = 2, padx = 10 )

Party_A_Sign.grid( row = 5, column = 1, padx = 10 )
Party_B_Sign.grid( row = 5, column = 2, padx = 10 )

#Date
label5.grid( row = 6, column = 1, padx = 10 )
Date.grid( row = 6, column = 2, padx = 10 )

#Buttons
b1.grid( row = 7, column = 1, columnspan = 2)
b2.grid( row = 8, column = 1, columnspan = 2)
#Static Properties
master.title('Algorand Smart Contract')
