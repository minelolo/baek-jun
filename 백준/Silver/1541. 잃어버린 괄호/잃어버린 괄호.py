equation = input().split('-')
number = []
for i in equation:
    number_2 = sum(map(int, i.split('+')))
    number.append(number_2)
first = number[0]
for i in number[1:]:
    first -= i
print(first)