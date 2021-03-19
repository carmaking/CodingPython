1)
N, M = map(int, input().split())
a=[]
for _ in range(0,N):
  data=list(map(int, input().split()))
  mindata=min(data)
  a.append(mindata)
  
print(max(a))

2)
N, M = map(int, input().split())

result=0

for _ in range(N):
  data=list(map(int, input().split()))
  mindata=min(data)
  result=max(result,mindata)

print(result)

3)
N, M = map(int, input().split())

result=0
min_value = 10001

for _ in range(N):
  data=list(map(int, input().split()))
  for a in data:
    min_value=min(min_value,a)
  result=max(result,min_value)

print(result)
