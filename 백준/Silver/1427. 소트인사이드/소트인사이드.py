n = list(map(int, input()))

n.sort(reverse = True)

result = ''.join(str(s) for s in n)
print(result)