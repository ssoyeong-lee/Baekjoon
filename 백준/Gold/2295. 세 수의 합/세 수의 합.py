import sys
input = sys.stdin.readline

n = int(input())
u = list(int(input()) for _ in range(n))
u.sort()

two = []
for i in range(n):
    for j in range(n):
        two.append(u[i] + u[j])
two = list(set(two))
two.sort()

def bs(target):
    start = 0; end = len(two)
    while start <= end:
        mid = (start + end) // 2
        if two[mid] == target:
            return True
        elif two[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for l in range(n - 1, 0, -1):
    for k in range(l + 1):
        if bs(u[l] - u[k]):
            print(u[l])
            exit(0)
