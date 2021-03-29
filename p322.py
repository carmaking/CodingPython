S = input()

alpha = []
num = []

for i in range(len(S)):
  if ord(S[i]) >= 65:
    alpha.append(S[i])
  else:
    num.append(int(S[i]))

alpha.sort()

for i in range(len(alpha)):
  print(alpha[i],end='')
  if i == len(alpha) - 1:
    print(str(sum(num)))
