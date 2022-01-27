# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:32:00 2022
Author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
from jax import float0
import functions as ft
from termcolor import colored
import sys
import os
import math as mt
from numpy import Infinity

#################################################
#     Main program
#################################################
def main():
    inf = Infinity
    
    try:
        print( "Now you will have to enter real and imaginary part of the wave-function you want to normalize. Some notes:" )
        print( "NB: enter each mathematical function as \"mt.function\" (ex: mt.cos(), mt.exp(), etc...)." )
        print()
        
        wave_real: str = input( "Enter the REAL part: " )
        wave_imag: str = input( "Enter the IMAGINARY part: " )
        
        print()
        print( "Now you will have to enter the integration extremes for the wave-function integrals calculation:" )
        print( "NB: infinity value is indicated with \"inf\"." )
        print()
        
        int_a: float = float( input( "Enter the lowest integration extreme: " ) )
        if int_a is str:
            int_a = float( int_a )
            
        int_b: float = float( input( "Enter the highest integration extreme: " ) )
        if int_b is str:
            int_b = float( int_b )

        if not ft.orthogonality( wave_real, wave_imag, int_a, int_b ):
            raise RuntimeError( colored( "Entered wave-function is not orthogonal!", "red" ) )
        
        if ft.orthonormality( wave_real, wave_imag, int_a, int_b ):
            raise RuntimeError( colored( "Entered wave-function is already normalized!", "red" ) )
        
    except RuntimeError as r:
        print()
        print( r )
        print()
        os.execl( sys.executable, sys.executable, *sys.argv ) 

if __name__ == "__main__":
    main()