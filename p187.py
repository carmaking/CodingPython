#순차 탐색
def sequential_search(n, target, array):

  for i in range(n):
    if array[i] == target:
      return i + 1

print("생성할 원소 개수, 한 칸 띄고 찾을 문자열")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열 입력")
array = input().split()

print(sequential_search(n, target, array))
