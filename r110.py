def move(N, step):
  x, y = 1, 1
  moving = ['L', 'R', 'U', 'D']
  movx = [0, 0, -1, 1]
  movy = [-1, 1, 0, 0]
  
  for i in range(len(step)):
    for j in range(4):
      if step[i] == moving[j]:
        changex = x + movx[j]
        changey = y + movy[j]
        if changex > 0 and changex <= N and changey > 0 and changey <= N:
          x, y = changex, changey
        break
  return print(x,y, end=' ')

N = int(input())

step = list(input().split())
move(N,step)
