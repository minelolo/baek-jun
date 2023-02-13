import sys

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    san = set(int(sys.stdin.readline()) for _ in range(n))
    sun = [int(sys.stdin.readline()) for _ in range(m)]
        
    cnt = 0
    
    for j in sun:
        if j in san:
            cnt += 1
            
    print(cnt)