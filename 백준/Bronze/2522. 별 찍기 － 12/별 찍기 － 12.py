m = int(input())

for i in range(1,m):
    print(('*'*i).rjust(m))
for i in range(m):
    print(('*'*(m-i)).rjust(m))