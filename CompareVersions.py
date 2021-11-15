def func(v1, v2):
  v1 = v1.split(".")
  v2 = v2.split(".")
  
  for i in range( min(len(v1), len(v2)) ):
    if int(v1[i]) > int(v2[i]):
      return 1
    elif int(v1[i]) < int(v2[i]):
      return -1
  
  if len(v1) == len(v2):
    return 0

  return 1 if len(v1)>len(v2) else -1
  
# v1 = '1.2.3.0'
# v2 = '1.2.3'

# print(func(v1,v2))
