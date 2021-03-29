S = list(map(int,input()))

temp = S[0]
count0 = 0
count1 = 0

if temp == 0:
  count0 += 1
else:
  count1 += 1

for i in S:
  if i == temp:
    continue
  else:
    temp = i

    if temp == 0:
      count0 += 1
    else:
      count1 += 1
    

print(min(count0, count1))
