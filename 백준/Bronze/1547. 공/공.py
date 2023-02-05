gong = ['o', 'x', 'x']

m = int(input())

for i in range(m):
    a,b = map(int, input().split())
    gong[a-1], gong[b-1] = gong[b-1], gong[a-1]

if 'o' in gong:
    print(gong.index('o') + 1)
else:
    print(-1)