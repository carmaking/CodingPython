N = input()

sumleft = 0
sumright = 0

for i in range(len(N)//2):
  sumleft += int(N[i])
  sumright += int(N[i+(len(N)//2)])

if sumleft == sumright :
  print("LUCKY")
else:
  print("READY")
