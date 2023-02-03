mal = list(input() for i in range(8))
pan = []
for i in range(8):
    if i % 2 != 0:
        pan.append([0,1,0,1,0,1,0,1])
    else:
        pan.append([1,0,1,0,1,0,1,0])
        
cnt = 0
for k in range(len(pan)):
    for s in range(len(mal)):
        if pan[k][s] == 1 and  mal[k][s] == 'F':
            cnt += 1
        else:
            cnt += 0

print(cnt)