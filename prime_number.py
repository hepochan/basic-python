a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
def prime(x):
    n=2
    if x==1:
        print("1は素数ではない")
    else :
        while x>=n:
            if n==x:
                print(f"{x}は素数である")
                break            
            if x%n==0:
                print(f"{x}は素数ではない")
                break
            else :
                n+=1

c=int(a)
d=int(b)
prime(c)
prime(d)