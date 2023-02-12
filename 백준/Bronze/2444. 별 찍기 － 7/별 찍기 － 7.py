m = int(input())
for i in range(1,m):
    print(" "*(m-i) + (('*')*(2*i-1)))
for i in range(m, 0, -1):
    print(" "*(m-i) + (('*')*(2*i-1)))