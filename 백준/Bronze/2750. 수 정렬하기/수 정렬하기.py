n = int(input())

num = []
for i in range(n):
    a = int(input())
    num.append(a)
    
num = sorted(num)

for i in num:
    print(i)