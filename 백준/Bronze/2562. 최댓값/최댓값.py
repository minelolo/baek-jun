bin_list = []
for i in range(0,9):
    bin_list.append(int(input()))
    
print(max(bin_list))
print(bin_list.index(max(bin_list))+1)