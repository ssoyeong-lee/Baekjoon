def func(a):
    if a == 0:
        return 0
    ret = str(a)
    while len(ret) < 4:
        ret += str(a)
    return int(ret[:4])
    
def solution(numbers):
    numbers.sort(key=func, reverse=True)
    return str(int(''.join(map(str, numbers))))