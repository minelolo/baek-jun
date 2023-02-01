stack = []

def push(self):
    stack.append(self)
def Pop():
    if len(stack) != 0:
        print(stack[-1])
        stack.pop()
    else:
        print(-1)
def size():
    print(len(stack))
def empty():
    if len(stack) != 0:
        print(0)
    else:
        print(1)
def top():
    if len(stack) != 0:
        print(stack[-1])
    else: 
        print(-1)
        
n = int(input())
bin_list = []
for i in range(n):
    bin_list.append(input())
    
for s in bin_list:
    if 'push' in s:
        for_push = list(map(str, s.split()))
        push(int(for_push[-1]))
    elif s == 'pop':
        Pop()
    elif s == 'size':
        size()
    elif s == 'empty':
        empty()
    else:
        top()
