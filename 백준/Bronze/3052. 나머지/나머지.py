A = [int(input()) for s in range(10)]
B = 42

namugi = []
for i in A:
    namugi.append(i%B)
    
result = []
for i in namugi:
    if i not in result:
        result.append(i)
        
print(len(result))