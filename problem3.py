def checkPrime(n): 
  p = 2
  while p*p <= n: 
    if (n % p == 0):
      return False
    p += 1
  return True

#print(checkPrime(100))

def largestPrimeFactor(n): 
  f = 2
  num = n
  while f*f <= num:  
    if (num % f == 0): 
      num /= f
    else: 
      f += 1
  return int(num)

print(largestPrimeFactor(600851475143))
