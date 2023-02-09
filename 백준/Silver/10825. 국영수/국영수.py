n = int(input())

ban = []
for i in range(n):
    data = input().split()
    ban.append((data[0], int(data[1]), int(data[2]), int(data[3])))
               
result = sorted(ban, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in result:
    print(i[0])