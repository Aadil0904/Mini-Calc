#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 20:34:13 2021

@author: aadilshaikh
"""

import tkinter as tk
from tkinter import Entry
from tkinter import Label
from tkinter import Button

def clearEntryBox():
    myEntryNo1.delete(0,len(myEntryNo1.get()))
    myEntryNo2.delete(0,len(myEntryNo2.get()))
    myEntryAns.delete(0,len(myEntryAns.get()))

def find(op):
    n1=int(myEntryNo1.get())
    n2=int(myEntryNo2.get())
    if op=='+':
        ans=n1+n2
    elif op=='-':
        ans=n1-n2
    elif op=='*':
        ans=n1*n2
    elif op=='/':
        ans=int(n1/n2)
    else:
        ans=n1%n2

    myEntryAns.delete(0,len(myEntryAns.get()))
    myEntryAns.insert(0,str(ans))
    
myWindow=tk.Tk()
myWindow.title("Mini-Calc")
myWindow.geometry("650x400")

myLabelTitle=Label(myWindow,text="MINI-CALC",padx=100,pady=15,bg='blue',fg='yellow',bd=10,relief='sunken',font='System')
myLabelTitle.grid(row=0,column=1)


myLabelMsg1=Label(myWindow,text="First Number ",padx=50,pady=10)
myLabelMsg1.grid(row=1,column=0)

myEntryNo1=Entry(myWindow,width=15)
myEntryNo1.grid(row=1,column=1)

myLabelMsg2=Label(myWindow,text="Second Number ",padx=50,pady=10)
myLabelMsg2.grid(row=2,column=0)

myEntryNo2=Entry(myWindow,width=15)
myEntryNo2.grid(row=2,column=1)


myLabelAns=Label(myWindow,text="Answer ",padx=50,pady=10)
myLabelAns.grid(row=3,column=0)
myEntryAns=Entry(myWindow,width=15)
myEntryAns.grid(row=3,column=1)

myLabelSpace=Label(myWindow,text="")
myLabelSpace.grid(row=4,column=0)

myButtonSum=Button(myWindow,text="Sum",padx=20,pady=10, command=lambda:find('+'))
myButtonSum.grid(row=5,column=0)

myButtonDifference=Button(myWindow,text="Difference",padx=20,pady=10, command=lambda:find('-'))
myButtonDifference.grid(row=5,column=1)

myButtonProduct=Button(myWindow,text="Product",padx=20,pady=10, command=lambda:find('*'))
myButtonProduct.grid(row=5,column=2)

myLabelSpace.grid(row=6,column=0)

myButtonQuotient=Button(myWindow,text="Quotient",padx=20,pady=10, command=lambda:find('/'))
myButtonQuotient.grid(row=7,column=0)

myButtonClear=Button(myWindow,text="Clear",padx=20,pady=10, command=clearEntryBox)
myButtonClear.grid(row=7,column=1)

myButtonRemainder=Button(myWindow,text="Remainder",padx=20,pady=10, command=lambda:find('%'))
myButtonRemainder.grid(row=7,column=2)

myWindow.mainloop()