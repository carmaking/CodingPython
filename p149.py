n, m = map(int, input().split())

#2차원 리스트 맵 정보
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())))


#DFS로 모든 노드 방문
def dfs(x, y):
  #주어진 범위 벗어나면 종료
  if x <= -1 or x >= n or y <= -1 or y >= m:
    return False
  #현재 노드 미방문 시
  if graph[x][y] == 0:
    graph[x][y] = 1
    #상하좌우 재귀적으로 호출. -> 연결된 노드들을 방문하여 1로 만들기 위함
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True
  return False


result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1

print(result)
