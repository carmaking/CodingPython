N = int(input())

array = list(map(int, input().split()))
array.sort()

num = 1

for x in array:
  if num < x:
    break
  num += x

print(num)
