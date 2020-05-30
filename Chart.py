"""
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- Chart.py

Description:
- This module defines the Chart class which creates graphical visuals.
Specifically it creates a chart object and has methods for scatter 
plots on those charts
"""
import portfolio
import Instrument
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter


class Chart:
    """This class defines a chart object"""
    def __init__(self, port, precision):
        #Instatntiates a list object of data points for a chart
        self.port = port
        if(type(port) is list):
            self.lis = [p.calc(precision) for p in port]
        else:
            self.lis = port.calc(precision)

    def scatter(self, page):
        """Calculates a scatter plot and displays it on the given 
        page"""
        #adds data points
        x, y = [], []
        for row in self.lis:
            x.append(row[2])
            y.append(row[1])

        #creates a figure
        ff = Figure(figsize=(4,4), dpi=90)

        #adds a plot
        a = ff.add_subplot(111)
        a.plot(x,y,label="combos",alpha=0.5)
        a.axis([0,0.2,0,0.2])

        #displays the figure
        canvas=FigureCanvasTkAgg(ff, page)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tkinter.BOTH,expand=True)
        

    def scatters(self, size=5):
        """Calculates multiple scatter plots from its self.port and 
        displays them as a graphical object."""
        #adds data points
        for index in range(len(self.port)):
            x, y = [], []
            for row in self.lis[index]:
                x.append(row[2])
                y.append(row[1])
            plt.scatter(x,y, s=size)

        #creates and displays graph
        plt.title("Asset Allocation: 2-Asset Portfolios")
        plt.xlabel("Risk")
        plt.ylabel("Returns")
        plt.show()