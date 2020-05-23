def collatzSeq(n): 
  num = n
  count = 1
  while num > 1: 
    if (num % 2 == 0): 
      num /= 2
    else: 
      num = 3*num + 1
    count += 1
  return count

def longestCollatz(n): 
  maxLen = 1
  for i in range(1,n): 
    collatz = collatzSeq(i)
    if (collatz > maxLen): 
      maxLen = collatz
      colNum = i
  return colNum

print(longestCollatz(1000000))
