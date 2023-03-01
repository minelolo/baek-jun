h, m = map(int, input().split())

if h == 0 and 0<= m <= 44:
    h = 23
    m += 15
elif 0<= m <= 44:
    h -= 1
    m += 15
elif 45<= m <= 59:
    h += 0
    m -= 45
    
print(h, m)