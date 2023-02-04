n = []
while True:
    a = input()
    n.append(a)
    if a == '0':
        break
        
width = 2

for i in range(len(n)-1):
    width += (len(n[i])-1)
    for s in n[i]:
        if s == '1':
            width += 2
        elif s == '0':
            width += 4
        else:
            width += 3
    print(width)
    width = 2