a, b = map(int, input().strip().split(' '))

top = max(a, b)
bottom = min(a, b)

# 합이 짝수면 높이 동일하게 맞출 수 있고 3 7 -> 5 5
# 합이 홀수면 최소 차이 1이 나야함 3 6 -> 4 5

if (top + bottom) % 2 != 0:
    print(1, top-((top+bottom)//2)-1)
else :
    print(0, top-((top+bottom)//2))
