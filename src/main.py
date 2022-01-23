# -*- coding: utf-8 -*-

"""
Created on Fri Jan 21 12:32:00 2022

@author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
import math as mt
from utils import Hermite

#################################################
#     Main program
#################################################
def f(n,x):
    return Hermite( x, n ) * mt.exp( - pow( x , 2 ) / 2 )

# Main function
def main():
    print (0.0031415926535897933/2)

# Main running
if __name__ == "__main__":
    main()