N, M, K = map(int, input().split())

array = list(map(int, input().split()))
array.sort()

first = array[-1]
second = array[-2]

a = M // (K+1)
total = (first * K + second) * a
total += first * (M - a * (K+1))

print(total)
