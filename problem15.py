def latticePath(n): 
  count = 1
  for i in range(1,n+1):
    count *= (2*n + 1 - i) / i
  return int(count) 

print(latticePath(20))
