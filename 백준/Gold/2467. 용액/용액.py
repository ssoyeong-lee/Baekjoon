import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

minVal = 2000000000
left_idx = right_idx = 0

for i in range(n - 1):
    cur = li[i]
    start = i + 1
    end = n - 1
    while start <= end:
        mid = (start + end + 1) // 2
        tmp = cur + li[mid]
        
        if abs(tmp) < minVal:
            minVal = abs(tmp)
            left_idx = i
            right_idx = mid
            if tmp == 0:
                break
        if tmp < 0:
            start = mid + 1
        else:
            end = mid - 1
    if li[left_idx] + li[right_idx] == 0:
        break;
print(li[left_idx], li[right_idx])
    