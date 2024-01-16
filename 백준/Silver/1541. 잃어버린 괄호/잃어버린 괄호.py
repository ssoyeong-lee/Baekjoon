expr = input().split('-')
total = []
for e in expr:
    nums = list(map(int, e.split('+')))
    total.append(sum(nums))

ret = total[0]
for i in range(1, len(total)):
    ret -= total[i]
print(ret)