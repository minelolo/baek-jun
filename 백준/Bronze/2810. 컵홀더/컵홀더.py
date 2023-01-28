n = int(input())
seats = input()

L = seats.count('L')

if L == 2:
    n += 0
elif L == 0:
    n += 0
else:
    for i in range(int(L/2) - 1):
        n -= 1

print(n)