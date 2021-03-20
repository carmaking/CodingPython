1)
N = int(input())

data = list(input().split())
x,y = 1, 1

#L,R,U,D 순서
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

a = ['L', 'R', 'U', 'D']

for plan in data:
  for i in range(len(a)):
    if plan == a[i]:
      x += dx[i]
      y += dy[i]
    if x < 1:
      x = 1
    elif x > N:
      x = N 
    elif y < 1:
      y = 1
    elif y > N:
      y = N

print(x, y)

2)
N = int(input())

data = list(input().split())
x,y = 1, 1

#L,R,U,D 순서
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

a = ['L', 'R', 'U', 'D']

for plan in data:
  for i in range(len(a)):
    if plan == a[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > N or ny > N:
    continue
  x, y = nx, ny
    
print(nx, ny)
