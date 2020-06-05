#Find the sum of the digits in the number 100!

def fds(n): 
  factorial = 1
  for i in range(2, n+1): 
    factorial *= i
  ls = []
  for digit in str(factorial): 
    ls.append(int(digit))
  output = 0
  for num in ls: 
    output += num
  return output

print(fds(100))
