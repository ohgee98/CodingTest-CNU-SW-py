# 다시풀기 - 시간초과

from string import ascii_lowercase

s = input().strip().lower()
q = int(input())

spell = list(ascii_lowercase)

answer = ""

for _ in range(q):
    a,b = map(int,input().strip().split(' '))

    temp = sorted(s[a-1:b])
    array = list(dict.fromkeys(temp))

    if spell==array:
        answer+="1"
    else:
        answer+="0"

print(answer)






