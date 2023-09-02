from math import sin
import math
# --example--
# print(sin(0))
# >>> 0
# -----------
n=100
h=(math.pi/(2*n))
S=0
for i in range(1,101):
    S=S+(h/2)*(sin(h*i-h)+sin(h*i))
print(S)