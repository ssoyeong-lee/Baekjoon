import sys

li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input().rstrip()

i = 0
for w in li:
    word = word.replace(w, 'a')

print(len(word))