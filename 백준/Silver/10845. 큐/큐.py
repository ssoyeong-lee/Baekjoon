from collections import deque

n = int(input())
ret= []
queue = deque()

for _ in range(n):
    cmd = input()
    if cmd == 'back':
        if len(queue) == 0:
            ret.append(-1)
        else:
            back = queue.pop()
            ret.append(back)
            queue.append(back)
    elif cmd == 'front':
        if len(queue) == 0:
            ret.append(-1)
        else:
            front = queue.popleft()
            ret.append(front)
            queue.appendleft(front)
    elif cmd == 'empty':
        if len(queue) == 0:
            ret.append(1)
        else:
            ret.append(0)
    elif cmd == 'size':
        ret.append(len(queue))
    elif cmd == 'pop':
        if len(queue) == 0:
            ret.append(-1)
        else:
            ret.append(queue.popleft())
    else:
        push, x = cmd.split()
        queue.append(x)
print(*ret, sep='\n')