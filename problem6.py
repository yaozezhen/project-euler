def sumSquareDiff(n): 
  nSum = 0
  nSquare = 0
  num = 0
  for i in range(n+1): 
    nSum += i*i 
    num += i
    nSquare = num*num 
  return (nSquare - nSum)

print(sumSquareDiff(100))
