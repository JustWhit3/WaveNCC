#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 12:33:00 2022
Author: Gianluca Bianco
"""

#################################################
#     Libraries
#################################################
import doctest
from termcolor import colored
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as sci
import arsenalgear.mathematics as mt

#################################################
#     "integral" function
#################################################
def integral( function, a, b ):
    """
    1-dimensional integral solution for finite and infinite bound conditions, using the Simpson rule.

    Args:
        a (any): lower integration extreme.
        b (any): higher integration extreme.
        function (any): integrand function.

    Returns:
        any: integral of the given function.
        
    Testing:
        >>> def test_integral( x ):
        ...     return x * np.exp( -pow( x, 2 ) )
        >>> def test_integral_2( x ):
        ...     return np.exp( -2 * pow( x, 2 ) )
        >>> def test_integral_3( x ):
        ...     return pow( x, 2 )
        >>> def test_integral_4( x ):
        ...     return np.exp( -x + 4 )
        >>> mt.IsInBounds( integral( test_integral, -np.Infinity, np.Infinity ), -0.001, 0.001 )
        True
        >>> mt.IsInBounds( integral( test_integral_2, -np.Infinity, np.Infinity ), 1.23, 1.25 )
        True
        >>> integral( test_integral_3, -np.Infinity, np.Infinity )
        Traceback (most recent call last):
            ...
        RuntimeError: \033[31mThe wave function integral is divergent!\033[0m
        >>> mt.IsInBounds( integral( test_integral_3, 1, 4 ), 19.5, 21.5 )
        True
        >>> mt.IsInBounds( integral( test_integral, 0, np.Infinity ), 0.49, 0.51 )
        True
        >>> mt.IsInBounds( integral( test_integral_2, -np.Infinity, 0 ), 0.61, 0.63 )
        True
        >>> mt.IsInBounds( integral( test_integral_4, 0, np.Infinity ), 54.1, 54.9 )
        True
    """
    
    if a == -np.Infinity or b == np.Infinity:
        inf = 0
        sup = np.pi
        
        if a != -np.Infinity and b == np.Infinity:
            inf = 0
            sup = np.pi / 2
        elif a == -np.Infinity and b != np.Infinity:
            inf = -np.pi / 2
            sup = 0
            
        var = lambda x: function( np.tan( x ) ) / pow( np.cos( x ), 2 )
        var_inf = function( np.tan( inf ) ) / pow( np.cos( inf ), 2 )
        var_sup = function( np.tan( sup ) ) / pow( np.cos( sup ), 2 )
    elif a != -np.Infinity and b != np.Infinity:
        inf = a
        sup = b
        var = lambda x: function( x )
        var_inf = function( inf )
        var_sup = function( sup )
    else:
        raise RuntimeError( colored( "Invalid integral bounds!", "red" ) )
    
    first = abs( sup - inf ) / 1000
    val = 1000 / 2
    result = 0
    
    for i in range( 1, int( val - 1 ) ):
        x = inf + 2 * i * first 
        result = result + 2 * var( x )
        
    for i in range( 1, int( val ) ):
        x = inf + ( 2 * i - 1 ) * first
        result = result + 4 * var( x )
        
    result = first * ( result + var_inf + var_sup ) / 3
    
    if result < -1e10 or result > 1e10:
        raise RuntimeError( colored( "The wave function integral is divergent!", "red" ) )
    else:
        return result

#################################################
#     "prod_integral" function
#################################################
def prod_integral( real_part, imaginary_part, m, n, a, b ):
    """
    Function used to compute the product integral between a wave function and is complex-conjugate.

    Args:
        real_part (any): real part of the given function.
        imaginary_part (any): imaginary part of the give function.
        m ([type]): wave-function index.
        n ([type]): wave-function index.
        a (any): lowest integral extreme.
        b (any): highest integral extreme.
        
    Returns:
        any: returns the product integral between a wave function and is complex-conjugate.
        
    Testing:
        Not necessary, since it is performed in the "orthogonality", "orthonormality" and "coefficients" functions.
    """
    
    function_product_real = lambda x: ( mt.e_parser( real_part, imaginary_part, m, x ).conjugate() * mt.e_parser( real_part, imaginary_part, n, x ) ).real
    function_product_imag = lambda x: ( mt.e_parser( real_part, imaginary_part, m, x ).conjugate() * mt.e_parser( real_part, imaginary_part, n, x ) ).imag
    product_integral = complex( integral( function_product_real, a, b ), integral( function_product_imag, a, b ) )
    
    return product_integral.real
    

#################################################
#     "orthogonality" function
#################################################
def orthogonality( real_part, imaginary_part, a, b ):
    """
    Function used to check if a given wave function is orthogonal.

    Args:
        real_part (any): real part of the given function.
        imaginary_part (any): imaginary part of the give function.
        a (any): lowest integral extreme.
        b (any): highest integral extreme.
        
    Returns:
        bool: returns the bool condition for the function orthogonality.
        
    Testing:
        >>> orthogonality( "Hermite( x, n ) * np.exp( - pow( x , 2 ) / 2 )", "0", -np.Infinity, np.Infinity )
        True
        >>> orthogonality( "n * np.exp( -pow( x , 2 ) / 2 )", "0", -np.Infinity, np.Infinity )
        False
        >>> orthogonality( "np.exp( -2 * abs( x ) ) * pow( np.sin( n ), 2 ) * x", "0", -np.Infinity, np.Infinity )
        True
        >>> orthogonality( "np.sin( n * np.pi * x )", "0", 0, 1 )
        True
        >>> orthogonality( "np.sin( n * np.pi * x )", "0", 0, 1 )
        True
        >>> orthogonality( "np.cos( n * np.pi * x )", "0", 0, 1 )
        True
    """
    
    arr = np.array([])
    m_ = 5
    n_ = 5
    
    for m in range( m_ ):
        for n in range( n_ ):
            if m == 0 and n == 0:
                continue
            res = round( prod_integral( real_part, imaginary_part, m, n, a, b ) )

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
#     "orthonormality" function
#################################################
def orthonormality( real_part, imaginary_part, a, b ):
    """
    Function used to check if a given wave function is orthonormal.

    Args:
        real_part (any): real part of the given function.
        imaginary_part (any): imaginary part of the give function.
        a (any): lower integral extreme.
        b (any): upper integral extreme.
        
    Returns:
        bool: returns the bool condition for the function orthonormality.
        
    Testing:
        >>> orthonormality( "np.sqrt( 2 ) * np.sin( n * np.pi * x )", "0", 0, 1 )
        True
        >>> orthonormality( "np.sqrt( n ) * np.exp( -n * abs( x ) )", "0", 0, np.Infinity )
        True
        >>> orthonormality( "Hermite( x, n ) * np.exp( - pow( x , 2 ) / 2 )", "0", -np.Infinity, np.Infinity )
        False
        >>> orthonormality( "np.sin( n * np.pi * x )", "0", 0, 1 )
        False
    """

    arr = np.array([])
    m_ = 5
    n_ = 5

    for m in range( m_ ):
        for n in range( n_ ):
            if m == 0 and n == 0:
                continue
            res = round( prod_integral( real_part, imaginary_part, m, n, a, b ) )

            if res == mt.kronecker( m, n ):
                arr = np.append( arr, True )
            else:
                arr = np.append( arr, False )
                
    if False in arr:
        return False
    else:
        return True
    
#################################################
#     "coefficients" function
#################################################
def coefficients( real_part, imaginary_part, a, b, n ):
    """
    Function used to compute the normalization coefficients.

    Args:
        real_part (any): real part of the given function.
        imaginary_part (any): imaginary part of the give function.
        a (any): lower integral extreme.
        b (any): upper integral extreme.
        n (int): wave function index.
        
    Returns:
        any: returns the value of the normalization coefficients.
        
    Testing:
        >>> round( coefficients( "Hermite( x, n ) * np.exp( - pow( x , 2 ) / 2 )", "0", -np.Infinity, np.Infinity, 1 ), 2 )
        0.53
        >>> round( coefficients( "Hermite( x, n ) * np.exp( - pow( x , 2 ) / 2 )", "0", -np.Infinity, np.Infinity, 3 ), 2 )
        0.11
        >>> round( coefficients( "np.sin( n * np.pi * x )", "0", 0, 1, 2 ), 2 )
        1.41
        >>> round( coefficients( "np.cos( x )", "np.sin( x )", -1, 1, 0 ), 2 )
        0.71
    """
    
    res = prod_integral( real_part, imaginary_part, n, n, a, b )
    denominator = np.sqrt( res.real )
    
    if denominator == 0:
        return colored( "Error, division by 0!", "red" )
    else:
        return 1 / denominator.real

#################################################
#     "plotter_complex" function
#################################################
def plotter_complex( real_part, imaginary_part, a, b, n, coefficient ):
    """
    Function used to plot a given wave-function for an index n.

    Args:
        real_part (string): mathematical real expression part.
        imaginary_part (string): mathematical imaginary expression part.
        a (any): lower integration extreme.
        b (any): higher integration extreme.
        n (int): wave function index.
        coefficient (any): value of the normalization coefficient.

    Returns:
        plot: the wave-function plot for the index n is returned.
    """
    
    if coefficient != colored( "Error, division by 0!", "red" ):
        
        if a == -np.inf and b != np.inf:
            x = np.arange( -10, b, ( ( b+10 ) / 10 ) )
        elif a != -np.inf and b == np.inf:
            x = np.arange( a, 10, ( ( 10-a ) / 10 ) )
        elif a == -np.inf and b == np.inf:
            x = np.arange( -10, 10, ( ( 20 ) / 10 ) )
        else:
            x = np.arange( 10*a, 10*b, ( ( 10*( b-a ) ) / 10 ) )

        def func( x ):
            return coefficient * mt.e_parser( real_part, imaginary_part, n, x )
        
        my_label = "Normalized wave-function f(x) for n = " + str( n )
        plt.figure( figsize = ( 8, 6 ), dpi = 80 )
        plt.xlabel( "Re: f(x)" )
        plt.ylabel( "Im: f(x)" )
        plt.title( my_label )

        if real_part == "0" and imaginary_part != "0":
            X_Y_Spline = sci.make_interp_spline( x, np.imag( func( x ) ) )
            X = np.linspace( x.min(), x.max(), 500 )
            Y = X_Y_Spline( X )
        
            plt.xlabel( "x" )
            plt.ylabel( "Im: f(x)" )
            plt.plot( X, Y, color = "green" )
        elif real_part != "0" and imaginary_part == "0":
            X_Y_Spline = sci.make_interp_spline( x, np.real( func( x ) ) )
            X = np.linspace( x.min(), x.max(), 500 )
            Y = X_Y_Spline( X )
        
            plt.xlabel( "x" )
            plt.ylabel( "Re: f(x)" )
            plt.plot( X, Y, color = "green" )
        else:
            X = np.real( func( x ) )
            Y = np.imag( func( x ) )
            tck, u = sci.splprep( [ X, Y ], s = 0 )
            unew = np.arange( 0, 1.01, 0.01 )
            out = sci.splev( unew, tck )
            
            plt.plot( X, Y, 'x', out[0], out[1], color = "green" )

        plt.show()

#################################################
#     Doing tests
#################################################
if __name__ == "__main__":
    doctest.testmod()