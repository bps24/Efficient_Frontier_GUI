"""
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- Instrument.py

Description:
- This module defines the Instrument class which stores financial 
instruments as objects storing their attributes.
"""
class Instrument:
    """This class stores financial instruments"""
    def __init__(self, ret, risk, name, t):
        """Creates a financial instrument"""
        self.name = name
        self.ret = ret
        self.risk = risk
        self.type = t

    def __str__(self):
        """Displays the string representation 
        of the financial instrument"""
        return ("Name: %s; Type: %s; Return: %s; Risk: %s" % (self.name, self.type, self.ret, self.risk))