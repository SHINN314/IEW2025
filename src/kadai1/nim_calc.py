import mex

def nim_sum(a, b):
  return a ^ b

def nim_mult_prime(a, b):
  if(a == 0 and b == 0):
    return 0
  
  T = []
  
  for a_prime in range(0, a):
    for b_prime in range(0, b):
      t = nim_sum(nim_mult_prime(a_prime, b), nim_mult_prime(a, b_prime))
      t = nim_sum(t, nim_mult_prime(a_prime, b_prime))

      if(not(t in T)):
        T.append(t)

  return mex.mex(T)

def nim_mult(a, b, memo):
  """
  Calculate multiple of nim.

  Values
  ----------
  a: int
    One of the value of nim multiple.

  b: int
    One of the value of nim multiple.

  memo: list
    Used for memoized recursive function.
    All elements of list is -1.

  Returns
  ----------
  i: int
    Result of calculated nim multiple.
  """

  # base case
  if(a == 0 and b == 0):
    memo[a][b] = 0
    return 0

  # induction steps
  T = []

  # check is nim_mult(a, b) was calculated
  if(memo[a][b] == -1):
    for a_prime in range(0, a):
      for b_prime in range(0, b):
        t = nim_sum(nim_mult(a_prime, b, memo), nim_mult(a, b_prime, memo))
        t = nim_sum(t, nim_mult(a_prime, b_prime, memo))

        if(not(t in T)):
          T.append(t)

  memo[a][b] = mex.mex(T)

  return memo[a][b]