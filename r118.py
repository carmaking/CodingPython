def direction():
  global direct
  direct -= 1
  if direct == -1:
    direct = 3

n , m =map(int, input().split())
A, B, direct = map(int, input().split())

array = []
for _ in range(n):
  array.append(list(map(int, input().split())))

stepA = [-1, 0, 1, 0]
stepB = [0, 1, 0, -1]
count = 1
check = 0
array[A][B] = 1

while 1:
  direction()
  newA = A + stepA[direct]
  newB = B + stepB[direct]

  if array[newA][newB] == 0:
    check = 0
    array[newA][newB] = 1
    count += 1
    A, B = newA, newB
  else:
    check += 1
    if check == 4:
      newA = A - stepA[direct]
      newB = B - stepB[direct]
      if array[newA][newB] == 1:
        break
      else:
        A, B = newA, newB
        check = 0

print(count)
