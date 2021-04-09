import math

def inv(x,m): #Returns an inverse of x mod m
    for i in range(m):
        if x*i % m == 1:
            return i

def product(X): #Product of an array
    p = 1
    for x in X:
        p = p*x
    return p

def crt(r,m): #Residues and modulos, as arrays - Chinese Remainder Theorem
    #Follows the proof of 4.13 in Elementary Number Thy, Rosen
    #r are the a_1, ..., a_r - name chosen before noticing index

    Mt = product(m) #M in the book
    M = [int(Mt/mk) for mk in m] #An array of the different M_k's
    print("M_k's    :",M)
    print('" mod m_k:',[Mk % mk for (Mk,mk) in zip(M,m)])
    y = [inv(Mk%mk,mk) for (Mk,mk) in zip(M,m)]
    print("y_k's    :",y)
    x = sum([product(list(p)) for p in zip(r,M,y)]) #x = a_1M_1y_1+...+a_rM_ry_r
    print("x =",x,"=",x%Mt,"mod",Mt)
    return x%Mt
