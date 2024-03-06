import sys
input = sys.stdin.readline

n = int(input())
left = {}
right = {}

for i in range(n):
  n, l, r = input().split()
  if l != '.':
    left[n] = l
  if r != '.':
    right[n] = r

preRet = []
def preorder(start='A'):
  preRet.append(start)
  if start in left:
    preorder(left[start])
  if start in right:
    preorder(right[start])

inRet = []
def inorder(start='A'):
  if start in left:
    inorder(left[start])
  inRet.append(start)
  if start in right:
    inorder(right[start])

postRet = []
def postorder(start='A'):
  if start in left:
    postorder(left[start])
  if start in right:
    postorder(right[start])
  postRet.append(start)

preorder()
inorder()
postorder()

print(''.join(preRet), ''.join(inRet), ''.join(postRet), sep='\n')