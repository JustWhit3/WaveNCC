# -*- coding: utf-8 -*-

"""
Created on Fri Jan 21 12:33:00 2022

@author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
import math as mt
import doctest
from termcolor import colored
import utils as ut
import numpy as np

#################################################
#     "orthogonality" function
#################################################
def orthogonality( real_part, imaginary_part, a, b ):
    """
    Function used to check if a given wave function, depending on a polynomial, can be normalized or not.

    Args:
        real_part (any): real part of the given function
        imaginary_part (any): imaginary part of the give function
        
    Returns:
        bool: returns the bool condition for the function normalization.
        
    Testing:
        >>> orthogonality( "Hermite( x, n ) * mt.exp( - pow( x , 2 ) / 2 )", "0", -np.Infinity, np.Infinity )
        True
        >>> orthogonality( "n * mt.exp( -pow( x , 2 ) / 2 )", "0", -np.Infinity, np.Infinity )
        False
        >>> orthogonality( "mt.exp( -2 * abs( x ) ) * pow( mt.sin( n ), 2 ) * x", "0", -np.Infinity, np.Infinity )
        True
        >>> orthogonality( "mt.sin( n * mt.pi * x )", "0", 0, 1 )
        True
        >>> orthogonality( "mt.sin( n * mt.pi * x )", "0", 0, 1 )
        True
        >>> orthogonality( "mt.cos( n * mt.pi * x )", "0", 0, 1 )
        True
    """
    
    arr = np.array([])
    m_ = 5
    n_ = 5
    
    for m in range( m_ ):
        for n in range( n_ ):
            function_product_real = lambda x: ( ut.e_parser( real_part, imaginary_part, m, x ).conjugate() * ut.e_parser( real_part, imaginary_part, n, x ) ).real
            function_product_imag = lambda x: ( ut.e_parser( real_part, imaginary_part, m, x ).conjugate() * ut.e_parser( real_part, imaginary_part, n, x ) ).imag
            product_integral = complex( ut.integral( function_product_real, a, b ), ut.integral( function_product_imag, a, b ) )
            res = round( product_integral.real )

            if m != n:
                if res == 0:
                    arr = np.append( arr, True )
                else:
                    arr = np.append( arr, False )
    
    if False in arr:
        return False
    else:
        return True
        
#################################################
#     Doing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()