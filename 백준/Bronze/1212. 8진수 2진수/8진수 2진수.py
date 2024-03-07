li = ['000', '001', '010', '011', '100', '101', '110', '111']
num = input()
ret = [''] * len(num)
for i in range(len(num)):
  ret[i] = li[int(num[i])]
final = ''.join(ret)
final = final.lstrip('0')
if final != '':
  print(final)
else:
  print('0')
