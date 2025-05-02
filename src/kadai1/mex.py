def mex(T):
  i = 0

  while((i in T)):
    i += 1

  return i

if __name__=="__main__":
  T = [1, 2]
  mex = mex(T)
  print(mex)