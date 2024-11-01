cnt = 0
target = 0
numbers = []

def backtracking(val, idx):
    global cnt
    if idx == len(numbers):
        if val == target:
            cnt += 1
        return
    
    backtracking(val + numbers[idx], idx + 1)
    backtracking(val + numbers[idx] * -1, idx + 1)
    
def solution(ns, t):
    global target, numbers
    target = t
    numbers = ns
    backtracking(0, 0)
    return cnt