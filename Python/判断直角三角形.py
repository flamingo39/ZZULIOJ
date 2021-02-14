a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
    print("yes")
else:
    print("no")
