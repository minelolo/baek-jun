m = int(input())

for i in range(1, m+1): #1~2n
    print('*' * i + ' ' * (m - i) + ' ' * (m - i) + '*' * i)
for i in range(m-1, 0, -1): # n-1 ~ 1
    print('*' * i + ' ' * (m - i) + ' ' * (m - i) + '*' * i)