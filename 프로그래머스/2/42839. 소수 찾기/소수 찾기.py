primes = [True] * 10000000

def calc_primes(end):
    primes[0] = primes[1] = False
    for i in range(2, end):
        if primes[i] == False:
            continue
        for j in range(i + i, end, i):
            primes[j] = False

answer = 0
number = set()
def backtracking(numbers, is_selected, tmp):
    global answer
    
    n = int(''.join(tmp)) if len(tmp) > 0 else 0
    if primes[n] and n not in number:
        answer += 1
        number.add(n)
    
    if len(tmp) == len(numbers):
        return
    
    for i in range(len(numbers)):
        if not is_selected[i]:
            is_selected[i] = True
            tmp.append(numbers[i])
            backtracking(numbers, is_selected, tmp)
            tmp.pop()
            is_selected[i] = False
    
    
    
def solution(numbers):
    numbers = [n for n in numbers]
    numbers.sort(reverse=True)
    end = int(''.join(numbers)) + 1
    calc_primes(end)
    backtracking(numbers, [False] * len(numbers), [])
    return answer