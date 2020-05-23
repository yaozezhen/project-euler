def findDivisor(n): 
  divisor = 0
  if (n == 1): 
    return 1
  for i in range(2,int(n/2)+1): 
    if (n % i == 0): 
      divisor += 1
  return (divisor + 2)

#Highly divisible triangle number
def HDTN(n): 
  trigNum = 1
  count = 2
  while findDivisor(trigNum) <= n: 
    trigNum += count
    count += 1
  return trigNum

print(HDTN(5))
    
