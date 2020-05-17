def checkPrime(n): 
  p = 2
  while p*p <= n: 
    if (n % p == 0):
      return False
    p += 1
  return True

def nthPrimeNum(n): 
  count = 0
  num = 1
  while count < n: 
    num += 1
    if (checkPrime(num) == True): 
      count += 1
  return num

print(nthPrimeNum(10001))
