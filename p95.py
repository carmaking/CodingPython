N, M ,K=map(int, input().split())

data=list(map(int, input().split()))
data.sort()

first=data[-1]
second=data[-2]

count=0
count=int(M/(K+1))*K
count+=M%(K+1)

result=count*first
result+=(M-count)*second
print(result)
