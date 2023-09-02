n=int(input("n="))

# TODO
def prime(n):
    m=2
    if n<=1:
        return False
    elif type(n)!=int:
        return False
    else :
        while n>=m:
            if m==n:
                return True           
            if n%m==0:
                return False
            else :
                m+=1
print(prime(n))