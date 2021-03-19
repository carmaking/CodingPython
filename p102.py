1)
N, K = map(int,input().split())
count = 0

while(N!=1):
  if(N%K):
    N-=1
  else:
    N/=K
  count+=1

print(count)

2)
N, K = map(int,input().split())
result = 0

while N >= K:
  while N % K != 0:
    N -= 1
    result += 1
  N //= K
  result += 1

while N > 1:
  N -= 1
  result += 1

print(result)

3)
N, K = map(int,input().split())
result = 0

while True:
  target = (N//K) * K
  result += N - target
  N = target

  if N < K:
    break
  
  result +=1
  N //= K

result += N-1
print(result)
