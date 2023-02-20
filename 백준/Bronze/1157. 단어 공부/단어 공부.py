string = input().upper()

dict_ = {}

for i in 'ABCDEFGHIJKLMNOPQRSVUTWXYZ':
    dict_[i] = 0
    
for i in string:
    if i in dict_:
        dict_[i] += 1
    else:
        dict_[i] += 0
        
tmp = [k for k,v in dict_.items() if max(dict_.values()) == v]

if len(tmp) > 1:
    print('?')
else:
    print(*tmp)