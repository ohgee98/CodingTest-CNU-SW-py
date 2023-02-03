w, h = map(int,input().strip().split(" "))

matrix = [[0 for _ in range(w)] for _ in range(h)]

f = int(input())
feed = []
for _ in range(f):
    i,j = map(int,input().strip().split(" "))
    feed.append([i,j])

order = input().strip().split(" ")

# 우측 R, 좌측 L, 북측 U, 남측 D
x = [-1,1,0,0]
y = [0,0,-1,1]
row = 0
col = 0
score = 0
idx = 0

for i in order:
    if i=="L":
        row += x[0]
        col += y[0]
    elif i=="R":
        row += x[1]
        col += y[1]
    elif i=="U":
        row += x[2]
        col += y[2]
    else:
        row += x[3]
        col += y[3]

    if col<h and row<w:
        if col==feed[idx][0] and row==feed[idx][1]:
            score += 1
            idx +=1
            print(score)
        else:
            print(score)
    else:
        print(-1)
        break