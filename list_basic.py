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
    i = 0
    answer = []

    while (True):

        if (i // 2 < len1) and (i // 2 < len2):

            if (i % 2 == 0):
                answer.append(arr1[i // 2])
            else:
                answer.append(arr2[i // 2])
            i += 1
        else:
            j = i // 2

            if len1 < len2:
                answer.extend(arr2[j:len2])

            elif len2 < len1:
                answer.extend(arr1[j:len1])

            break

    print(*answer)