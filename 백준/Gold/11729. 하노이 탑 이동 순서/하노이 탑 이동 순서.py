
n = int(input())

li = []
def hanoi(start, mid, end, n):
    global li
    if n == 0:
        return
    hanoi(start, end, mid, n - 1)
    li.append([start, end])
    hanoi(mid, start, end, n - 1)

hanoi (1, 2, 3, n)
print(len(li))
for s, e in li:
    print(s, e)