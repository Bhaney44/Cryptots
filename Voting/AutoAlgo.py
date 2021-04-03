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

#Nodes
label0 = Label(master, text = 'Node 0', relief = 'groove', width = 20)
label1 = Label(master, text = 'Node 1', relief = 'groove', width = 20)
label2 = Label(master, text = 'Node 2', relief = 'groove', width = 20)
label3 = Label(master, text = 'Stake', relief = 'groove', width = 20)
label4 = Label(master, text = 'Vote', relief = 'groove', width = 20)
label5 = Label(master, text = 'Return', relief = 'groove', width = 20)

#Stake
Stake0 = Entry(master, relief = 'groove', width = 20)
Stake1 = Entry(master, relief = 'groove', width = 20)
Stake2 = Entry(master, relief = 'groove', width = 20)

#Vote
Vote0 = Entry(master, relief = 'groove', width = 20)
Vote1 = Entry(master, relief = 'groove', width = 20)
Vote2 = Entry(master, relief = 'groove', width = 20)

#Return
Return0 = Entry(master, relief = 'groove', width = 20)
Return1 = Entry(master, relief = 'groove', width = 20)
Return2 = Entry(master, relief = 'groove', width = 20)


#write to file function
def consensus():
    #Add votes
        Vote00 = int(Vote0.get())
        Vote11 = int(Vote1.get())
        Vote22 = int(Vote2.get())
        total_up_votes = Vote00 + Vote11 + Vote22
        #Stake
        Stake00 = int(Stake0.get())
        Stake11 = int(Stake1.get())
        Stake22 = int(Stake2.get())
        Total_Stake = Stake00 + Stake11 + Stake22
        #Return
        if total_up_votes > 1:
                Return00 = Stake00/Total_Stake * 10
                Return0.insert(0, Return00)
                Return11 = Stake11/Total_Stake * 10
                Return1.insert(0, Return11)
                Return22 = Stake22/Total_Stake * 10
                Return2.insert(0, Return22)
                
        else:
            print("Zero")
            Return0.insert(0, 0)
            Return1.insert(0, 0)
            Return2.insert(0, 0)



def clear():
    Return0.delete(0, END)
    Return1.delete(0, END)
    Return2.delete(0, END)
    Stake0.delete(0, END)
    Stake1.delete(0, END)
    Stake2.delete(0, END)
    Vote0.delete(0, END)
    Vote1.delete(0, END)
    Vote2.delete(0, END)



#Button to run write
b1 = Button(master, text = 'Calculate Consensus', relief = 'groove', width = 25, command=consensus)
b2 = Button(master, text = 'New Vote', relief = 'groove', width = 25, command=clear)

#Geometry
#Labels
label0.grid( row = 1, column = 2, padx = 10 )
label1.grid( row = 1, column = 3, padx = 10 )
label2.grid( row = 1, column = 4, padx = 10 )
label3.grid( row = 2, column = 1, padx = 10 )
label4.grid( row = 3, column = 1, padx = 10 )
label5.grid( row = 4, column = 1, padx = 10 )

#Stake
Stake0.grid( row = 2, column = 2, padx = 10 )
Stake1.grid( row = 2, column = 3, padx = 10 )
Stake2.grid( row = 2, column = 4, padx = 10 )

#Vote
Vote0.grid( row = 3, column = 2, padx = 10 )
Vote1.grid( row = 3, column = 3, padx = 10 )
Vote2.grid( row = 3, column = 4, padx = 10 )

#Return
Return0.grid( row = 4, column = 2, padx = 10 )
Return1.grid( row = 4, column = 3, padx = 10 )
Return2.grid( row = 4, column = 4, padx = 10 )

#Buttons
b1.grid( row = 5, column = 2, columnspan = 2)
b2.grid( row = 6, column = 2, columnspan = 2)

#Static Properties
master.title('Automating Consensus Protocol')
