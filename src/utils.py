# System libraries
from multiprocessing.sharedctypes import Value
import parser
from math import cos, pi 

# Other libraries
import doctest

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
#     "expression_parser" function
#################################################
def expression_parser( real_part, imaginary_part, n, x ):
    """
    Returns the complex value of a parsed expression.

    Args:
        real_part (string): mathematical real expression part.
        imaginary_part (string): mathematical imaginary expression part.
        n (int): wave function index.
        x (double): expression variable.

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

#def integral( f ):
    
    
#################################################
#     Performing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()