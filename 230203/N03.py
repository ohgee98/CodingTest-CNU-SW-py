n = int(input())
siso = list(map(int, input().strip().split(' ')))

if n == 1:
    print(1)
else:
    i = 0
    flag = True
    for i in range(len(siso)):
        left = sum(siso[:i])
        right = sum(siso[i + 1:])

        if left == right:
            print(i + 1)
            flag = False
            break

    if flag:
        print(-1)
