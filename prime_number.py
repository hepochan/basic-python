a = input("aの値を入力: ")
b = input("bの値を入力: ")

# TODO
c=int(a)
d=int(b)
for i in range(2,c):
    if c%i==0:
        print("aは素数ではない")
        break
print("aは素数")
for i in range(2,d):
    if d%i==0:
        print("bは素数ではない")
        break
    print("bは素数")