x, y, w, h = map(int, input().split())

bin_list = []

bin_list.append(w-x)
bin_list.append(h-y)
bin_list.append(x-0)
bin_list.append(y-0)

print(min(bin_list))