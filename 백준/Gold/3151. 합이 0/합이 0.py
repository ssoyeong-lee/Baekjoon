import sys
from bisect import bisect_left, bisect_right

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
cache = set(numbers)
answer = 0
for i in range(N - 2):
    for j in range(i+1, N - 1):
        target = -(numbers[i] + numbers[j])
        if target in cache:
            answer += bisect_right(numbers, target, j+1) - bisect_left(numbers, target, j+1)

print(answer)