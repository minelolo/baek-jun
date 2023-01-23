n,k = map(int, input().split())
count = 0
money = []

for i in range(n):
    a = int(input())
    money.append(a)
    


money = list(reversed(money))

for m in money:
    b = k//m
    count += b
    k -= m * b
    
print(count)