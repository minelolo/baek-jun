eum = list(map(int, input().split()))

if eum == sorted(eum):
    print('ascending')
elif eum == sorted(eum, reverse = True):
    print('descending')
else:
    print('mixed')