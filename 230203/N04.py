#다시풀기 - 실패, 시간초과

n = int(input())
b = list(map(int, input().strip().split(' ')))
m = int(input())
q = list(map(int, input().strip().split(' ')))

total = 0
replay = sum(b)
i,j = 0,0
temp = b[0]
time = q[0]

while(True):

    if replay < time:
        time = time%replay
        j = 0
        temp = b[j]

    if time <= temp:
        total += j + 1
        i+=1
        if m <= i:
            break
        time = q[i]

    elif j < n :
        j+=1
        temp += b[j]

total = total%1000000007

print(total)
