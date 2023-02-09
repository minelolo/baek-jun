n = int(input())

bin_list = [input() for x in range(n)]

bin_list = list(set(bin_list))

bin_list.sort()

bin_list.sort(key=len)

for i in bin_list:
    print(i)