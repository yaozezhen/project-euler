def checkMultiple(numList, multiple): 
  for num in numList: 
    if (multiple % num != 0): 
      return False
  return True

def smallestMultiple(n): 
  multiple = n
  check = []
  for i in range(int(n/2)+1, n+1): 
    check.append(i)
  while checkMultiple(check, multiple) == False: 
    multiple += n
  return multiple

print(smallestMultiple(5))
