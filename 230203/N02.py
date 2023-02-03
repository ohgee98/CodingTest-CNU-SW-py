n,m = map(int, input().strip().split(' '))

temp = [i for i in range(1,n+1)]

for _ in range(m):
    u,v = map(int, input().strip().split(' '))

    change = temp[u-1]
    temp[u-1] = temp[v-1]
    temp[v-1] = change

print(*temp)