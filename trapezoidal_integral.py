from math import sin
# --example--
# print(sin(0))
# >>> 0
# -----------
h=(3.1415/(2*100))#piは3.1415とした
S=0
for i in range(1,100):
    S=S+(h/2)*(sin(h*i-h)+sin(h*i))
print(S)