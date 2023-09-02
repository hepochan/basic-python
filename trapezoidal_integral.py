from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# -----------
def integral(func,a,b,n):
    S=0
    h=(b-a)/n
    for i in range(1,n+1):
        S=S+(h/2)*(func(h*i-h)+func(h*i))
    return S
def f0(x):
    return sin(x)
def f1(y):
    return 4/(1+y**2)
def f2(z):
    return ((math.pi)**(1/2))*math.exp(-z**2)
print(integral(f0,0,math.pi/2,50))
print(integral(f1,0,1,100))
print(integral(f2,-100,100,1000))
