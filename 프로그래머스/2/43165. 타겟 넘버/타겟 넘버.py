cnt = 0
target = 0
numbers = []

def dfs(val, idx):
    global cnt
    if idx == len(numbers):
        if val == target:
            cnt += 1
        return
    
    dfs(val + numbers[idx], idx + 1)
    dfs(val + numbers[idx] * -1, idx + 1)
    
def solution(ns, t):
    global target, numbers
    target = t
    numbers = ns
    dfs(0, 0)
    return cnt