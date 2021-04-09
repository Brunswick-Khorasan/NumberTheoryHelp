import math

def pollardrho(x0,f,n):
        div = 1
        x = [0,x0,f(x0)%n]
        k = 1
        while div == 1 or div == n:
                print(x[1:]) #Ignore the leading 0, since everything else does too
                print("(x_",2*k," - x_",k,", ",n,")",sep='');
                div = gcd(abs(x[2*k]-x[k]),n)
                if div == 1 or div == n: #moves forwards if (x_2k,x_k)=1
                        x = x+[f(x[-1])%n]
                        x = x+[f(x[-1])%n]
                        print("appending")
                        k = k + 1
        print(n,"=",div,"*",int(n/div))

def rhohelp(x0,f,n):
        x = [x0]
        xn = x0
        while f(xn)%n not in x:
                x = x+[f(xn)%n]
                xn = f(xn)%n
        print(x+[f(xn)%n])
        return x+[f(xn)%n]

def gcd(a,b):
        (r,s) = (a,b)
        while r != 0 and s != 0:
                print((r,s))
                (r,s) = sgcd(r,s)
        return r+s

def sgcd(a,b):
        if b > a:
                a,b = b,a
        return (a-b*math.floor(a/b),b)

