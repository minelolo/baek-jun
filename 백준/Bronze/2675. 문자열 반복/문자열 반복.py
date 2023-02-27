t = int(input())
bin_list = []

for i in range(t):
    bin_list.append(list(input().split()))
    
for s in range(t):
    a = [x * int(bin_list[s][0]) for x in bin_list[s][1]]
    print(''.join(a))