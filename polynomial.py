__author__ = 'Nathaniel Klein - Coded on my MBPro - 06/04/15'

def eval(x, poly):
    """
    Evaluate the polynomial at the value x.
    poly is a list of coefficients from lowest to highest.

    :param x:     Argument at which to evaluate
    :param poly:  The polynomial coefficients, lowest order to highest
    :return:      The result of evaluating the polynomial at x
    """

    i = 0
    j = len(poly)
    val = 0
    while(i < j):
        val += poly[i] * pow(x,i)
        i += 1
    return val


def bisection(a, b, poly, tolerance):
    """
    Assume that poly(a) <= 0 and poly(b) >= 0.

    :param a: poly(a) <= 0  Raises an exception if not true
    :param b: poly(b) >= 0  Raises an exception if not true
    :param poly: polynomial coefficients, low order first
    :param tolerance: greater than 0
    :return:  a value between a and b that is within tolerance of a root of the polynomial
    """

    if(eval(a,poly) > 0):
        raise Exception("The value of the polynomial when evaluated at a is positive")
    if(eval(b,poly) < 0):
        raise Exception("The value of the polynomial when evaluated at b is negative")

    # tolerance measures the desired distance between a and b
    if(tolerance <= 0):
        raise Exception("The tolerance must be reset to a value greater than 0")

    while(abs(a-b)) > tolerance:
        mid = (a + b)/2
        if(eval(mid,poly) < 0):
            a = mid
        else:
            b = mid

    # A value between a and b that is within the tolerance of a root of the polynomial is returned
    return (a+b)/2