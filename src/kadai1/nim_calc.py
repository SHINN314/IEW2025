import mex

memo = {}

def nim_sum(a, b):
  return a ^ b

def nim_time_prime(a, b):
  if(a == 0 and b == 0):
    return 0
  
  T = []
  
  for a_prime in range(0, a):
    for b_prime in range(0, b):
      t = nim_sum(nim_time_prime(a_prime, b), nim_time_prime(a, b_prime))
      t = nim_sum(t, nim_time_prime(a_prime, b_prime))

      if(not(t in T)):
        T.append(t)

  return mex.mex(T)

def nim_time(a, b):
  result = 0
  while b:
    if b & 1:
      result ^= a 
    a <<= 1
    b >>= 1
  return result
