from sys import stdin
input = stdin.readline

NAME=0
KOREAN=1
ENGLISH=2
MATH=3

def solution(li):
  li.sort(key=lambda x: (-x[KOREAN], x[ENGLISH],-x[MATH], x[NAME]))
  return [x[NAME] for x in li]

n = int(input())
li = []
for _ in range(n):
  name, korean, english, math = input().split()
  li.append([name, int(korean), int(english), int(math)])
print(*solution(li), sep='\n')