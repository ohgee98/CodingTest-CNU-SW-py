N = int(input().strip())
data = list(map(int,input().strip().split(" ")))
Q = int(input().strip())

for _ in range(Q):
    a,b = map(int,input().strip().split(" "))

    if a==b :
        print(data[a])
    else:
        print(sum(data[a-1:b-1]))