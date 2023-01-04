T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int,input().strip().split(' ')))
    i = 1

    while(i!=len(A)) :
        if A[i] < A[i-1] :
            A.pop(i)
        else:
            i+=1

    print(*A)
