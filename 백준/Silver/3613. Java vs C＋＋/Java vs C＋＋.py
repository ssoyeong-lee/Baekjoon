def isJava(varName):
  if not ('a' <= varName[0] <= 'z'):
    return False
  for j in varName:
    if not ('a' <= j <= 'z' or 'A' <= j <= 'Z'):
      return False
  return True

def isCpp(varName):
  tag = False
  if varName[0] == '_' or varName[-1] == '_':
    return False
  for c in varName:
    if tag and c == "_":
      return False
    if c == '_':
      tag = True
    elif 'a' <= c <= 'z':
      tag = False
    else:
      return False
  return True

def cppToJava(varName):
  ret = [] ; tag = False
  for c in varName:
    if c == '_':
      tag = True
    elif tag:
      ret.append(c.upper())
      tag = False
    else:
      ret.append(c)
  return ''.join(ret)

def javaToCpp(varName):
  ret = []
  for c in varName:
    if 'a' <= c <= 'z':
      ret.append(c)
    elif 'A' <= c <= 'Z':
      ret.append('_')
      ret.append(c.lower())

  return ''.join(ret)

varName = input().rstrip()
if isJava(varName):
  print(javaToCpp(varName))
elif isCpp(varName):
  print(cppToJava(varName))
else:
  print('Error!')