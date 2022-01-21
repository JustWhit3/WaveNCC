# -*- coding: utf-8 -*-

# System libraries
import parser
from math import sin, cos, pi 

# Other libraries
import doctest

#################################################
#     Global variables
#################################################
inf = 0
sup = 2*pi

#################################################
#     Testing functions
#################################################
def test_integral( n, x ):
    """
    Function used for testing only.
    """
    
    return pow( sin( x ), n ) - cos( x )

def test_integral_2( n, x ):
    """
    Function used for testing only.
    """
    
    return pow( x, n )

#################################################
#     "colorr" class
#################################################
class color:
    """
    Class to manage output stream colors and styles.
    """
    
    red = "\033[31m"
    reset = "\033[0m"
    
#################################################
#     "IsInBounds" function
#################################################
def IsInBounds( value, min, max ):
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
    
    if min < value < max:
        return True
    return False

#################################################
#     "expression_parser" function
#################################################
def expression_parser( real_part, imaginary_part, n, x ):
    """
    Returns the complex value of a parsed expression.

    Args:
        real_part (string): mathematical real expression part.
        imaginary_part (string): mathematical imaginary expression part.
        n (any): wave function index.
        x (any): expression variable.

    Returns:
        complex: returns the value of a complex parsed expression for an index n and variable x.
        
    Testing:
        >>> expression_parser( "pow( x, n )", "0", 2, 2 )
        (4+0j)
        >>> expression_parser( "n*cos( x )", "3*n", 2, pi )
        (-2+6j)
        >>> expression_parser( "n*cos( k )", "3*n", 2, pi )
        Traceback (most recent call last):
            ...
        NameError: name 'k' is not defined
        >>> expression_parser( "n*cos( x )", "3*z", 2, pi )
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
def integral( function, n ):
    """
    1-dimensional integral solution in the range [0,2*pi], using the Simpson rule.

    Args:
        function ([type]): [description]
        a ([type]): [description]
        b ([type]): [description]
        n ([type]): [description]

    Returns:
        [type]: [description]
        
    Testing:
        >>> IsInBounds( integral( test_integral, 2 ), 3.12, 3.16 )
        True
        >>> IsInBounds( integral( test_integral_2, 2 ), 82.1, 83.2 )
        True
    """
    
    nm = 1000
    first = ( sup - inf ) / nm
    val = nm / 2
    result = 0
    
    for i in range( 1, int( val - 1 ) ):
        x = inf + 2 * i * first
        result = result + 2 * function( n, x )
    for i in range( 1, int( val ) ):
        x = inf + ( 2 * i - 1 ) * first
        result = result + 4 * function( n, x )
    result = first * ( result + function( n, inf ) + function( n, sup ) ) / 3
        
    return result
    
    
#################################################
#     Performing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()