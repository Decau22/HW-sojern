import math

def getMin(lst, q=1):
  lst.sort()
  q = min(q, len(lst))
  return lst[:q-1]

def getMax(lst, q=1):
  lst.sort(reverse=True)
  q = min(q, len(lst))
  return lst[:q-1]

def getAvg(lst):
  return sum(lst) / len(lst)

def getMedian(lst):
  lst.sort()
  half = len(lst) // 2
  if len(lst) % 2 == 0:
    return (lst[half - 1] + lst[half]) / 2
  return lst[half]

def getPercentile(lst, p):
  lst.sort()
  n = math.ceil((len(lst) * p) / 100)
  return lst[ n - 1]

# a = [15,20,35,40,50]
# print(getPercentile(a, 30))