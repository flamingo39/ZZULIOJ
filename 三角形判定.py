a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a + b > c and a + c > b and b + c > a:
    print("Yes")
else:
    print("No")
