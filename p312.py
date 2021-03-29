S = list(map(int,input()))

result = 1

if sum(S) == 0:
  print(0)

else:
  for i in S:
    if i != 0:
      result *= i

  print(result)
