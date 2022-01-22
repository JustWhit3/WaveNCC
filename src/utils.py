# -*- coding: utf-8 -*-

#################################################
#     Libraries
#################################################
import parser
import math as mt
import doctest
from termcolor import colored

#################################################
#     Testing functions
#################################################
def test_integral( x ):
    """
    Function used for testing only.
    """
    
    n = 2
    return x * mt.exp( -pow( x, 2 ) )

def test_integral_2( x ):
    """
    Function used for testing only.
    """
    
    n = 2
    return mt.exp( -2 * pow( x, 2 ) )

def test_integral_3( x ):
    """
    Function used for testing only.
    """
    
    n = 2
    return pow( x, 2 )

def Hermite( x, n ):
    """
    Function used for testing only.
    """
    
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x * Hermite( x, n-1 ) - 2 * ( n-1 ) * Hermite( x, n-2 )
    
def H_non( x, n ):
    """
    Function used for testing only.
    """
    
    if n == 0:
        return 1
    elif n == 1:
        return 2 * x
    else:
        return 2 * x
    
#################################################
#     "IsInBounds" function
#################################################
def IsInBounds( value, min_, max_ ):
    """
    Function to check if a value is in certain bounds.

    Args:
        value (any): the interested value.
        min (any): min value.
        max (any): max value.

    Returns:
        bool: return true if is in the bound, otherwise false.
        
    Testing:
        >>> IsInBounds( 3, 1, 5 )
        True
        >>> IsInBounds( 2.3, -2, 3 )
        True
        >>> IsInBounds( 1, 2, 3 )
        False
    """
    
    if min_ < value < max_:
        return True
    return False

#################################################
#     "expression_parser" function
#################################################
def e_parser( real_part, imaginary_part, n, x ):
    """
    Returns the complex value of a parsed expression.

    Args:
        real_part (string): mathematical real expression part.
        imaginary_part (string): mathematical imaginary expression part.
        n (int): wave function index.
        x (any): expression variable.

    Returns:
        complex: returns the value of a complex parsed expression for an index n and variable x.
        
    Testing:
        >>> e_parser( "pow( x, n )", "0", 2, 2 )
        (4+0j)
        >>> e_parser( "n*mt.cos( x )", "3*n", 2, mt.pi )
        (-2+6j)
        >>> e_parser( "n*mt.cos( k )", "3*n", 2, mt.pi )
        Traceback (most recent call last):
            ...
        NameError: name 'k' is not defined
        >>> e_parser( "n*mt.cos( x )", "3*z", 2, mt.pi )
        Traceback (most recent call last):
            ...
        NameError: name 'z' is not defined
    """
    
    real_p = parser.expr( real_part ).compile()
    imag_p = parser.expr( imaginary_part ).compile()
    
    return complex( eval( real_p ), eval( imag_p ) )

#################################################
#     "integral" function
#################################################
def integral( function ):
    """
    1-dimensional integral solution in the range [-inf,inf], using the Simpson rule.

    Args:
        function (any): integrand function

    Returns:\033[31m
        any: integral of the given function
        
    Testing:
        >>> IsInBounds( integral( test_integral ), -0.001, 0.001 )
        True
        >>> IsInBounds( integral( test_integral_2 ), 1.23, 1.25 )
        True
        >>> integral( test_integral_3 )
        Traceback (most recent call last):
            ...
        RuntimeError: \033[31mThe wave function integral diverges!\033[0m
    """
    
    inf = 0
    sup = mt.pi
    first = ( sup - inf ) / 1000
    val = 1000 / 2
    result = 0
    
    for i in range( 1, int( val - 1 ) ):
        x = inf + 2 * i * first
        result = result + 2 * function( mt.tan( x ) ) / pow( mt.cos( x ), 2 )
    for i in range( 1, int( val ) ):
        x = inf + ( 2 * i - 1 ) * first
        result = result + 4 * function( mt.tan( x ) ) / pow( mt.cos( x ), 2 )
        
    result = first * ( result + ( function( mt.tan( inf ) ) / pow( mt.cos( inf ), 2 ) ) + ( function( mt.tan( sup ) ) / pow( mt.cos( sup ), 2 ) ) ) / 3
    
    if result < -1e10 or result > 1e10:
        raise RuntimeError( colored( "The wave function integral diverges!", "red" ) )
    else:
        return result

#################################################
#     "kronecker" function
#################################################
def kronecker( i, j ):
    """
    Definition of the Kronecker delta function for two numbers i and j.

    Args:
        i (int): index i
        j (int): index j

    Returns:
        int: return the Kronecker delta value.
        
    Testing:
        >>> kronecker( 2, 2 )
        1
        >>> kronecker( 1, 2 )
        0
    """
    
    if i == j:
        return 1
    else:
        return 0
    
#################################################
#     Doing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()