n = int(input())
dasom = int(input())
poll = [int(input()) for i in range(n-1)]
people = 0
if n != 1:
    while True:
        a = poll.index(max(poll))
        if dasom <= max(poll):
            dasom += 1
            poll[a] -= 1
            people += 1
        else:
            break
    print(people)
else:
    print(0)
