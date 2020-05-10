import math 

def checkPalindromic(n): 
  numList = [int(x) for x in str(n)]
  reverseNum = list(reversed(numList))
  if (numList == reverseNum): 
    return True
  return False

#Find the largest palindrome made from the product of two 3-digit numbers.

def LPP(n): 
  i = 0
  j = 0
  while i * i <= n: 
    while j * j <= n: 
      product = (int(math.sqrt(n)) - i) * (int(math.sqrt(n)) - j)
      if checkPalindromic(product) == True: 
        return product
      j += 1
    i += 1
      
print(LPP(999*999))
