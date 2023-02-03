# 풀이 중
t1 = input()
t2 = input()

if len(t1) == 0:
    print(t2)

elif len(t2) == 0:
    print(t1)

else:

    arr1 = list(map(int, t1.strip().split(" ")))
    arr2 = list(map(int, t2.strip().split(" ")))

    len1 = len(arr1)
    len2 = len(arr2)
    answer = []
    Min = min(len1, len2)

    for i in range(Min):
        answer.append(arr1[i])
        answer.append(arr2[i])

    if len1 < len2:
        answer.extend(arr2[Min:len2])
    elif len2 < len1:
        answer.extend(arr1[Min:len1])

    print(*answer)