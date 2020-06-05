#Evaluate the sum of all the amicable numbers under 10000.

#Find the sum of proper divisors of n
def d(n): 
  output = 0
  d = 1
  while 2*d <= n: 
    if (n % d == 0): 
      output += d
    d += 1
  return output

#Find sum of amicable numbers
def san(n): 
  dic = {}
  output = 0
  for i in range(n): 
    dic[i] = d(i)
  for i in range(n-1): 
    for j in range(i+1,n): 
      if (i == dic[j] and j == dic[i]): 
        output += (i+j)
  return output

print(san(10000))
