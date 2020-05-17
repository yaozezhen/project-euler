def checkPrime(n): 
  p = 2
  while p*p <= n: 
    if (n % p == 0):
      return False
    p += 1
  return True

def primeSum(n): 
  pSum = 0
  for i in range(2,n): 
    if (checkPrime(i) == True): 
      pSum += i
  return pSum

print(primeSum(2000000))
