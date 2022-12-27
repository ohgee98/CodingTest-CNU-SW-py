def rotate(key,r):
    n = len(key)
    result = [[0] * n for _ in range(n)]
    if r==0:
        result = key
    else :
        result = key[::-1]

    return result

def attach(x,y,m,use_key,lock_fild):
    for i in range(m):
        for j in range(m):
            lock_fild[x+i][y+j] += use_key[i][j]

def detach(x,y,m,use_key,lock_fild):
    for i in range(m):
        for j in range(m):
            lock_fild[x+i][y+j] -= use_key[i][j]


def unlock(lock_fild,m,n):
    for i in range(n):
        for j in range(n):
            if lock_fild[m+i][m+j] != 1:
                return False
    return True

def lockKey(key,lock) :
    m = len(key)
    n = len(lock)
    lock_fild = [[0] * (m*2+n) for _ in range(m*2+n)]

    for i in range(n):
        for j in range(n):
            lock_fild[m + i][m + j] = lock[i][j]

    for i in range(1, n * 2):
        for j in range(1, n * 2):

            for r in range(2):
                use_key = rotate(key, r)

                for x in range(1,m+n):
                    for y in range(1,m+n):
                        attach(x,y,m,use_key,lock_fild)

                        if unlock(lock_fild,m,n):
                            return True

                        detach(x,y,m,use_key,lock_fild)

    return False


key = []
lock = []
flag = False

m, n = map(int, input().strip().split(' '))

for _ in range(m):
    key.append(list(map(int, input().strip().split(' '))))

for _ in range(n):
    lock.append(list(map(int, input().strip().split(' '))))

if lockKey(key,lock):
    print("true")
else:
    print("false")


