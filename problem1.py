# Adding all multiples of 7 and 11 less than or equal to 1000
def sevenEleven(n): 
  result = 0
  for i in range(1, n+1): 
    if (i % 7 == 0) or (i % 11 == 0): 
      result += i
  return result

print (sevenEleven(1000))
