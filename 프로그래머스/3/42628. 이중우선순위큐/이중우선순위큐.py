def solution(operations):
    li = []
    for operation in operations:
        cmd, num = operation.split()
        if cmd == 'I':
            li.append(int(num))
        elif cmd == 'D':
            if len(li) > 0 and num == '-1':
                li.sort(reverse=True)
                li.pop()
            elif len(li) > 0 and num == '1':
                li.sort()
                li.pop()
    li.sort()
    return [0, 0] if len(li) == 0 else [li[-1], li[0]]
                