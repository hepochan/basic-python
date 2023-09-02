a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
c=int(a)
d=int(b)
if c<d :
    c=int(b)
    d=int(a)
e=c%d
if e==0:
    print(f"最大公約数は{d}")
else:
    while e!=0:
        c,d=d,e
        e=c%d
    print(f"最大公約数は{d}")
