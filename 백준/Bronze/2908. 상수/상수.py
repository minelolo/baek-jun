num = list(map(int, input().split()))
bin_list = []
for i in num:
    new_num = str(i)
    bin_list.append(new_num[::-1])
    
print(max(bin_list))