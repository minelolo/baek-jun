p = int(input())
dic = []
for i in range(p):
    a = list(map(int, input().split()))
    dic.append(a)
bin_list = []
cnt = 0

for i in range(p):
    if dic[i][1:] != dic[i][1:].sort():
        for _ in range(len(dic[i][1:])):
            for o in range(len(dic[i][1:])):
                o += 1
                if dic[i][o] == dic[i][-1]:
                    cnt += 0
                elif dic[i][o] > dic[i][o+1]:
                    dic[i][o],dic[i][o+1] = dic[i][o+1],dic[i][o]
                    cnt+=1
                else:
                    cnt+=0
        print(i+1, cnt)
        cnt = 0
    else:
        print(i+1, cnt)