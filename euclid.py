a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
def euclid(a,b):
    e=0
    if a<=0 or b<=0:
        return False
    elif type(a)!=int or type(b)!=int:
        return False
    else :
        if a<b:
            a,b=b,a
        e=a%b
        if e==0:
            return b
        else:
            while e!=0:
                a,b=b,e
                e=a%b
            return b
def mutually(a,b):
    if euclid(a,b)==1:
        return True
    else :
        return False
print(euclid(a,b))
print(f"a,bは互いに素である。{mutually(a,b)}")