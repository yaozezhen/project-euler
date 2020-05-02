# Adding all even Fibonacci numbers less than 4000000
def fibonacci(n): 
  fibList = [1,2]
  fibSum = 0
  while max(fibList) < n: 
    fibList.append(fibList[len(fibList) - 1] + fibList[len(fibList) - 2])
  for item in fibList: 
    if (item % 2 == 0): 
      fibSum += item
  return fibSum

print (fibonacci(4000000))
