"""
Step 06: Bonus

Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- run1.py

Description:
- This module defines the run1 class which displays the efficient 
frontier of asset allocations for a specific portfolio of assets 
composed of only two financial instruments.
"""
from Instrument import Instrument
from portfolio import Portfolio
from Chart import Chart

def main():
    """Defines assets, creates portfolios, and displays a scatter plot 
    of the different portfolios"""
    s1 = Instrument(0.01, 0.01, "Asset 1", "Equity")
    s2 = Instrument(0.02, 0.02, "Asset 2", "Bond")
    s3 = Instrument(0.03, 0.03, "Asset 3", "Commodity")
    s4 = Instrument(0.04, 0.04, "Asset 4", "Equity")

    p1 = Portfolio([s1, s2])
    p2 = Portfolio([s1, s3])
    p3 = Portfolio([s1, s4])
    p4 = Portfolio([s2, s3])
    p5 = Portfolio([s2, s4])
    p6 = Portfolio([s3, s4])

    p1.addcorr([[0,-0.1]])
    p2.addcorr([[0,-0.1]])
    p3.addcorr([[0,-0.1]])
    p4.addcorr([[0,-0.1]])
    p5.addcorr([[0,-0.1]])
    p6.addcorr([[0,-0.1]])

    c = Chart([p1,p2,p3,p4,p5,p6],0.004)
    c.scatters(size=3)



if __name__ == '__main__':
    main()