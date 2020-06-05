#Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

#Find the sum of proper divisors of n
def d(n): 
  output = 0
  d = 1
  while 2*d <= n: 
    if (n % d == 0): 
      output += d
    d += 1
  return output

#Find a list of all abundant numbers less than 28123. 
def abundant(): 
  ls = []
  for i in range(28124): 
    if (d(i) > i): 
      ls.append(i)
  return ls

#Find non-abundant sums
def nas(): 
  abSum = []
  abList = abundant()
  output = 0
  for i in range(len(abList)): 
    for j in range(len(abList)): 
      if (i+j not in abSum): 
        abSum.append(i+j)
  for i in range(28124): 
    if (i not in abSum): 
      output += i
  return output

print(nas())
