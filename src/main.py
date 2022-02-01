# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:32:00 2022
Author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
from operator import index
import sys, os
import functions as ft
from termcolor import colored
import cmath as mt
from cmath import pi
from numpy import Infinity

#################################################
#     Main program
#################################################
def main():
    #Global variables:
    inf = Infinity
    
    #Try block:
    try:
        #Initial messages:
        print( "Choose an option:" )
        print( "1. compute a single normalization coefficient for a given wave-function." )
        print( "2. compute all the values of the coefficients frm n to 0." )
        print( "3. quit the program." )
        print( "" )
        
        option = input( "Option choice: " )
        
        if option == "3":
            sys.exit()
        elif option == "1" or option == "2":
            pass
        else:
            raise RuntimeError( colored( "Invalid option!", "red" ) )
        
        print( "" )
        print( "Now you will have to enter real and imaginary part of the wave-function you want to normalize. Some notes:" )
        print( "1. enter each mathematical function as \"mt.function\" (ex: mt.cos(), mt.exp(), etc...)." )
        print( "2. if the real or the imaginary parts are null, enter 0 in its place." )
        print()
        
        wave_real: str = input( "Enter the " + colored( "REAL", "yellow" ) + " part: " )
        wave_imag: str = input( "Enter the " + colored( "IMAGINARY", "yellow" ) + " part: " )
        
        print()
        print( "Now you will have to enter the integration extremes for the wave-function integrals calculation:" )
        print( "NB: infinity value is indicated with \"inf\" and pi with \"pi\"." )
        print()
        
        int_a: float = float( input( "Enter the " + colored( "LOWEST", "yellow" ) + " integration extreme: " ) )
        
        #Trick to support pi and inf:
        if int_a is str:
            int_a = float( int_a )
            
        int_b: float = float( input( "Enter the " + colored( "HIGHEST", "yellow" ) + " integration extreme: " ) )
        
        #Trick to support pi and inf:
        if int_b is str:
            int_b = float( int_b )

        #Check if wave function is orthogonal or orthonormal:
        if not ft.orthogonality( wave_real, wave_imag, int_a, int_b ):
            raise RuntimeError( colored( "Entered wave-function is not orthogonal!", "red" ) )
        
        if ft.orthonormality( wave_real, wave_imag, int_a, int_b ):
            raise RuntimeError( colored( "Entered wave-function is already normalized!", "red" ) )
        
        #Return the normalization coefficients:
        print( "" )
        index: int = int( input( "Enter the wave-function index \"n\": " ) )
        
        if option == "1":
            coeff = ft.coefficients( wave_real, wave_imag, int_a, int_b, index )
            col_coeff = colored( coeff, "green" )
            print( "" )
            print( "The normalization coefficient for n = ", index, " is: ", col_coeff, "." )
            print( "" )
        else:
            print( "" )
            for nth in range( 0, index ):
                coeff = ft.coefficients( wave_real, wave_imag, int_a, int_b, nth )
                col_coeff = colored( coeff, "green" )
                print( "The normalization coefficient for n = ", nth, " is: ", col_coeff )
                print( "" )
            
        #Ask if want to compute other coefficients:
        while True:
            try:
                final_option = input( "Do you want to compute another index (y/n) ? " )
                if final_option == "y" or final_option == "Y":
                    print( "" )
                    os.execl( sys.executable, sys.executable, *sys.argv )
                elif final_option == "n" or final_option == "N" :
                    sys.exit()
                else:
                    raise RuntimeError( colored( "Invalid option!", "red" ) )
            except RuntimeError as r:
                print()
                print( r )
                pass
        
    #Catch the exceptions:
    except RuntimeError as r:
        print()
        print( r )
        print()
        os.execl( sys.executable, sys.executable, *sys.argv ) 

if __name__ == "__main__":
    main()