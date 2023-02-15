n = int(input())
s_card = list(map(int, input().split()))

m = int(input())
num = list(map(int, input().split()))

s_card.sort()

#result = [0]*m

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for i in num:
    a = binary_search(s_card, i, 0, n-1)
    if a != None:
        print("1", end = ' ')
    else:
        print("0", end = ' ')