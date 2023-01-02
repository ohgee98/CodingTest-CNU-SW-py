from collections import deque

m,n = map(int,input().strip().split(" ")) #m 가로 n 세로

tomato = [list(map(int,input().strip().split(" "))) for _ in range(n)]

queue = deque()

for row in range(n):
    for col in range(m):
        if tomato[row][col]==1:
            queue.append([row,col])


dx = [-1,1,0,0] # 왼쪽, 오른쪽 이동
dy = [0,0,-1,1] # 위, 아래 이동
answer = 0

while queue:
    x, y = queue.popleft()

    for i in range(4): # 방향 이동
        nx, ny = dx[i]+x, dy[i]+y

        if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny]==0:
            tomato[nx][ny] = tomato[x][y]+1
            queue.append([nx,ny])

for i in tomato:
    for j in i:
        if j==0:
            print(-1)
            exit(0)

    answer = max(answer, max(i))

print(answer-1)



