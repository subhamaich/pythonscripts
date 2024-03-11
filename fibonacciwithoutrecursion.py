fibs = [0,1]
def fibonacci(i):
  if i <= len(fibs)-1:
    return fibs[i]
  else:
    while i > len(fibs)-1:
      next_fib = fibs[-1]+fibs[-2]
      fibs.append(next_fib)
    return fibs[i]


# test cases
print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)