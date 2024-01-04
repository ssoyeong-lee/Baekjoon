import sys
input = sys.stdin.readline

n = int(input())
pattern = input().rstrip()
filenames = [input().rstrip() for _ in range(n)]

li = pattern.split('*')
for filename in filenames:
    if len(filename) < len(li[0]) + len(li[1]):
        print('NE')
    elif li[0] != '' and filename.find(li[0]) != 0:
        print('NE')
    elif li[-1] != '' and filename.rfind(li[1]) + len(li[-1]) != len(filename):
        print('NE')
    else:
        print('DA')