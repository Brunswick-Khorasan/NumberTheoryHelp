from math import *

def st_decomp(x):
    """
        Decomposition into x = 2**s * t
    """
    t = x
    s = 0
    while t % 2 == 0 and t > 1:
        s += 1
        t = t / 2
    return (s,int(t))

def miller(n,b):
    """
        Determines if n passes the Miller-Rabin test for a base b
    """
    s,t = st_decomp(n-1)
    if (b**t)% n == 1:
        return True
    for j in range(0,s):
        if (b**(2**j*t))%n == n-1:
            return True
    return False
