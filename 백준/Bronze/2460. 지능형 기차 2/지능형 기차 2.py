total = 0

people = []

for i in range(10):
    a, b = map(int,input().split())
    total += (-a)
    total += b
    people.append(total)

print(max(people))
