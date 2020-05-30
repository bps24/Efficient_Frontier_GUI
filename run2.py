"""
Step 06: Bonus
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- run2.py

Description:
- This module defines the run2 class which displays an interactice 
graph of the efficient frontier of two assets with sliders to change values"""

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from tkinter import *
from Instrument import Instrument
from portfolio import Portfolio
from Chart import Chart

class Window:
    """Defines a window whcih will pop up when ran"""
    def __init__(self, root):
        """Creates a window and builds the sliders and graph"""
        self.app=root
        self.app.geometry('800x500')
        self.app.title("Bryce Streeper: Asset Allocation Visual ")
        self.makeTitle()
        self.makeGraph()
        self.makeSliders()
        self.update()

    def makeTitle(self):
        """Creates and displays the graph title"""
        l1=Label(self.app, text="Asset Allocation Combinations")
        l1.grid(row=0, column=0)


    def makeGraph(self):
        """Creates and displauys the Efficient Fronier Graph"""
        self.graphFrame = Frame(height=400, width=400, bd=10, bg='black')
        self.graphFrame.grid(row=1, column=0)

    def makeSliders(self):
        """Creates and displays the sliders"""
        #Builds the frame for the sliders
        self.stockFrame = Frame(height=400, width=400, bd=10)
        self.stockFrame.grid(row=1, column=1)

        #Adds labels to the frame
        self.lab1= Label(self.stockFrame, text="Asset 1")
        self.lab1.grid(row=0, column=0, sticky=W)
        self.lab2= Label(self.stockFrame, text="            Return: ")
        self.lab2.grid(row=1, column=0, sticky=E)
        self.lab3= Label(self.stockFrame, text="            Risk: ")
        self.lab3.grid(row=2, column=0, sticky=E)
        self.lab4= Label(self.stockFrame, text="Asset 2")
        self.lab4.grid(row=3, column=0, sticky=W)
        self.lab5= Label(self.stockFrame, text="            Return: ")
        self.lab5.grid(row=4, column=0, sticky=E)
        self.lab6= Label(self.stockFrame, text="            Risk: ")
        self.lab6.grid(row=5, column=0, sticky=E)
        self.lab7= Label(self.stockFrame, text="Asset 1, Asset 2")
        self.lab7.grid(row=6, column=0, sticky=W, columnspan=2)
        self.lab8= Label(self.stockFrame, text="Covariance:")
        self.lab8.grid(row=7, column=0, sticky=E)

        #Adds the sliding bars to the frame
        self.r1 = Scale(self.stockFrame, from_=0, to=0.2, \
        resolution=0.01, orient=HORIZONTAL, length=200, \
        command=self.update, showvalue=0)
        self.s1 = Scale(self.stockFrame, from_=0, to=0.2, \
        resolution=0.01, orient=HORIZONTAL, length=200, \
        command=self.update, showvalue=0)
        self.r2 = Scale(self.stockFrame, from_=0, to=0.2, \
        resolution=0.01, orient=HORIZONTAL, length=200, \
        command=self.update, showvalue=0)
        self.s2 = Scale(self.stockFrame, from_=0, to=0.2, \
        resolution=0.01, orient=HORIZONTAL, length=200, \
        command=self.update, showvalue=0)
        self.p = Scale(self.stockFrame, from_=-1, to=1, \
        resolution=0.05, orient=HORIZONTAL, length=200, \
        command=self.update, showvalue=0)

        #Organizes all the sliders 
        self.r1.grid(row=1, column=2)
        self.s1.grid(row=2, column=2)
        self.r2.grid(row=4, column=2)
        self.s2.grid(row=5, column=2)
        self.p.grid(row=7, column=2)
        self.r1.set(0.12)
        self.s1.set(0.15)
        self.r2.set(0.07)
        self.s2.set(0.08)

        #Provides interactivity between sliders and graph
        self.r1_string = Label(self.stockFrame, text=self.r1.get())
        self.r1_string.grid(row=1, column=1)
        self.s1_string = Label(self.stockFrame, text=self.r1.get())
        self.s1_string.grid(row=2, column=1)
        self.r2_string = Label(self.stockFrame, text=self.r1.get())
        self.r2_string.grid(row=4, column=1)
        self.s2_string = Label(self.stockFrame, text=self.r1.get())
        self.s2_string.grid(row=5, column=1)
        self.p_string = Label(self.stockFrame, text=self.r1.get())
        self.p_string.grid(row=7, column=1)

    def update(self, *args):
        """Updates the graph with the altered sliders"""
        #Fetches slider information
        s1=self.s1.get()
        s2=self.s2.get()
        r1=self.r1.get()
        r2=self.r2.get()
        p=self.p.get()

        #Changes the number next to the bar
        self.r1_string.configure(text="%.2f"% r1)
        self.r2_string.configure(text="%.2f"% r2)
        self.s1_string.configure(text="%.2f"% s1)
        self.s2_string.configure(text="%.2f"% s2)
        self.p_string.configure(text="%.2f"% self.p.get())

        #Creates two asset objects
        self.I1 = Instrument(r1, s1, "Asset 1", "Equity")
        self.I2 = Instrument(r2, s2, "Asset 2", "Bond")

        #Builds a portfolio object
        self.port = Portfolio([self.I1, self.I2])
        self.port.addcorr([[0,p]])

        #Displays the new graph to the graph frame
        fff =Frame(height=400, width=400, bd=10, bg='white')
        Chart(self.port, 0.02).scatter(fff)
        fff.grid(row=1, column=0)

if __name__ == "__main__":
    #runs the tkinter application
    app = Tk()
    Window(app)
    app.mainloop()