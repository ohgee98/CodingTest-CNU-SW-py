n = int(input().strip())
co = []
for i in range(n):
    co.append(list(map(int, input().strip().split(' '))))

line = {}
check = []

for i in range(n):
    line = {}

    for j in range(i+1,n):

        if co[i][0] != co[j][0]:
            a = (co[j][1] - co[i][1]) / (co[j][0] - co[i][0]) #기울기
            b = co[i][1] - (a * co[i][0]) #절편

            if (a,b) in line:
                line[(a,b)] += 1
            else:
                line[(a,b)] = 2

        else:
            if co[j][0] in line :
                    line[co[j][0]] += 1
            else :
                line[co[j][0]] = 2

        if j==n-1:
            check.append(max(line.values()))

print(max(check))
