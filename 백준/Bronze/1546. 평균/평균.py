n = int(input())
score = list(map(int, input().split()))
score.sort()
best = max(score)

new_bin = []
for i in range(len(score)):
    new_bin.append((score[i]/best)*100)

print(sum(new_bin) / n)