from sys import stdin
input = stdin.readline

def solution(length, price):
  min_val = 1000000000; total = 0
  for i in range(len(length)):
    min_val = min(min_val, price[i])
    total += min_val * length[i]
  return total

input()
length = list(map(int, input().split()))
price = list(map(int, input().split()))
print(solution(length, price))