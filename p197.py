#이진탐색
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None


N = int(input())
a = list(map(int, input().split()))
a.sort()

M= int(input())
b = list(map(int, input().split()))

for i in b:
  result = binary_search(a, i, 0, N - 1)
  if result != None:
    print('yes', end = ' ')
  else:
    print('no', end = ' ')
    
    
#계수 정렬
N = int(input())
array = [0] * 1000001

for i in input().split():
  array[int(i)] = 1

M = int(input())
b = list(map(int, input().split()))

for i in b:
  if array[i] == 1:
    print('yes', end=' ')
  else:
    print('no', end=' ')
    

#집합 자료형
N = int(input())
array = set(map(int,input().split()))

M = int(input())
b = list(map(int, input().split()))

for i in b:
  if i in array:
    print('yes', end=' ')
  else:
    print('no', end=' ')
