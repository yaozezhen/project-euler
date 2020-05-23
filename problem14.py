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

#print(collatzSeq(9))

def longestCollatz(n): 
  maxLen = 1
  for i in range(1,n): 
    if (collatzSeq(i) > maxLen): 
      maxLen = collatzSeq(i)
  return maxLen

print(longestCollatz(1000000))
