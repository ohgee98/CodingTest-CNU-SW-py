n = int(input())
line = []
check = [[0]*3 for i in range(10000)]

check[1] = list(map(int,input().split(" ")))
for x in range(2,n+1):
    r, y, g = map(int,input().split(" "))

    check[x][0] = r + min(check[x-1][1],check[x-1][2])
    check[x][1] = y + min(check[x-1][0],check[x-1][2])
    check[x][2] = g + min(check[x - 1][0], check[x - 1][1])

print(min(check[n]))