from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))

#상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#BFS
def bfs(x, y):
  
  queue = deque()
  queue.append((x,y))

  while queue:
    x, y = queue.popleft()
    #현 위치에서 네 방향으로 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      #미로 공간 벗어나면 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      #벽이면 무시
      if graph[nx][ny] == 0:
        continue
      #해당 노드를 처음 방문할 때 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  #가장 오른쪽 아래까지 최단 거리 반환
  return graph[n-1][m-1]

#BFS 수행 결과 출력

print(bfs(0,0))
