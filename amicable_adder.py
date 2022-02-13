
def sum_amicables(max):
  
  
  def d(n:int) -> int:
  # makes the sum of proper divisors of n (numbers less than n which divide evenly into n)
    top = int(n/2) # since the biggest integer divisor of a number is its half.
    result = 0
    for i in range(1,top+1):
        if n%i == 0: 
            # evaluates if the rest of the division is zero
            result +=i
    return result
  
  # here starts the code to perform the sum of all amicable numbers lower than a paramm
  sum = 0
  for n1 in range(2, max+1):
    # includes the max in the for loop
    n2 = d(d(n1))
    # Optional line to debug the code:
    # print(f"n1: {n1}, d1:{d(n1)} and d(d1): {n2}, Amicable? {n1==n2}")
    if (n1 == n2):
      if (n2<=max):
      # Performs the sum only if n2 is less or equal than the max (in our case 10.000)
      # Only checks for n2, because size of n1 is controled by the for loop
        sum = sum + n1 + n2
  return sum


