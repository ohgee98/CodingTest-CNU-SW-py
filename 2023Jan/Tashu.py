T = int(input().strip())

for _ in range(T):
    N = int(input().strip()) # 대여소 개수
    A = list(map(int,input().strip().split(" "))) # 초기 대여소 자전거 개수
    M = int(input().strip()) # 이용 기록 개수

    for i in range(M):
        U,V = map(int,input().strip().split(" "))
        A[U-1] -= 1
        A[V-1] += 1

    print(*A)