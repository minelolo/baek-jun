n = int(input())
time = list(map(int, input().split()))
total = 0
indi_time = 0

time.sort()

for i in time:
    indi_time += i
    total += indi_time
    
print(total)