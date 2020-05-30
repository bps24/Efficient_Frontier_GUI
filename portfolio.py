"""
Title:
- 2020 Spring Capstone Project

Author:
- Bryce Streeper

Date:
- 2020 May 18

Filename:
- portfolio.py

Description:
- This module defines the Portfolio class which stores financial 
instruments and their respective risk, return, and correlation.
"""
import numpy as np
import random
import Instrument

class Portfolio:
    """Stores portfolio objects as a list of individual financial 
    instruments"""
    def __init__(self, inst):
        """Creates a portfolio object"""
        self.instruments = inst
        self.correlation = []
        self.ret , self.risk = [], []
        for i in inst:
            self.ret.append(i.ret)
            self.risk.append(i.risk)

    def addcorr(self, corr):
        """Add correlation coefficients to the portfolio as a list"""
        self.correlation = corr
        
    def calcret(self, weights):
        """Calculates and retunrs the expected return of its portfolio 
        given a specific weight distribution for assets"""
        return sum([w*r for w,r in zip(weights, self.ret)])

    def calcrisk(self, weights):
        """Calculates and returns the expected risk of its portfolio 
        given a specific weight distributioj for assets"""
        one = 0
        two = 0
        corr = self.correlation
        for weight, risk in zip(weights, self.risk):
            bb = weight * weight * risk * risk
            one += bb
        for i in range(len(corr)):
            for j in range(i+1, len(corr[0])):
                c = weights[i]*weights[j]*corr[i][j]*self.risk[i]*self.risk[j]
                two += c
        var = two * 2 +one
        risk = var ** 0.5
        return risk

    def calc(self, increment):
        """Returns a list of data points as [weight, return, risk] 
        for all weight distributions with a given weight increment """
        lis1 = []
        weights = self.set_weights(increment)
        for weight in weights:
            lis1.append([weight, self.calcret(weight), self.calcrisk(weight)])
        return lis1

    def set_weights(self, increment):
        """Helper method that returns a list of weight distribution 
        possibilities for a given incremental value"""
        if len(self.instruments)==2:
            return Portfolio.set_weights_double(increment)
        if len(self.instruments)==3:
            return Portfolio.set_weights_triple(increment)
        if len(self.instruments)==4:
            return Portfolio.set_weights_quad(increment)
        if len(self.instruments)==5:
            return Portfolio.set_weights_quint(increment)

    @staticmethod
    def set_weights_double(increment):
        """Static method that returns the weight distributions for a 
        portfolio with two assets with a given incremental value"""
        weights = []
        w1 = 0
        while w1 <= 1 and w1 >= 0:
            weights.append([round(w1,5), round(1-w1,5)])
            w1 += increment
        return weights

    @staticmethod
    def set_weights_triple(increment):
        """Static method that returns the weight distributions for a 
        portfolio with three assets with a given incremental value"""
        weights = []
        w1 = 0
        while w1 <= 1 and w1 >= 0:
            w2 = 0
            while w2 <= 1-w1 and w2 >= 0:
                weights.append([round(w1,5), round(w2,5), round(1-w1-w2,5)])
                w2 += increment
            w1 += increment
        return weights

    @staticmethod
    def set_weights_quad(increment):
        """Static method that returns the weight distributions for a 
        portfolio with four assets with a given incremental value"""
        weights = []
        w1 = 0
        while w1 <= 1 and w1 >= 0:
            w2 = 0
            while w2 <= 1-w1 and w2 >= 0:
                w3 = 0
                while w3 <= 1-w1-w2 and w3 >= 0:
                    weights.append([round(w1,5), round(w2,5), \
                    round(w3, 5), round(1-w1-w2-w3,5)])
                    w3 += increment
                w2 += increment
            w1 += increment
        return weights
        
    @staticmethod
    def set_weights_quint(increment):
        """Static method that returns the weight distributions for a 
        portfolio with five assets with a given incremental value"""
        weights = []
        w1 = 0
        while w1 <= 1 and w1 >= 0:
            w2 = 0
            while w2 <= 1-w1 and w2 >= 0:
                w3 = 0
                while w3 <= 1-w1-w2 and w3 >= 0:
                    w4 = 0
                    while w4 <= 1-w1-w2-w3 and w4 >= 0:
                        weights.append([round(w1,5), round(w2,5), \
                        round(w3, 5), round(w4, 5), round(1-w1-w2-w3-w4,5)])
                        w4 += increment
                    w3 += increment
                w2 += increment
            w1 += increment

        print(weights)
        return weights

    def __str__(self):
        """Returns the spring representation of the portfolio"""
        s=''
        for i in self.instruments:
            s+=("Name: %s; Type: %s; Return: %s; Risk: %s\n" % \
            (i.name, i.type, i.ret, i.risk))
        return s






