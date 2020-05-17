def pythagoreanTriplet(n): 
  for a in range(1, int(n/3)): 
    for b in range(a+1, int(n/2)): 
      if (a**2 + b**2 == (n-a-b)**2): 
        print(a, b, n-a-b)

pythagoreanTriplet(1000)
