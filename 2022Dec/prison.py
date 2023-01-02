p = int(input())
idx_p = list(map(int,input().strip().split(" ")))
l = int(input())
idx_l = list(map(int,input().strip().split(" ")))

temp = idx_p + idx_l
Max = max(temp)+1

prison = [ 0 * i for i in range(Max) ]

for i in idx_p:
    if i in idx_l:
        continue
    prison[i] = 1

idx = 0
count = 0

while(True):
    if 1 not in prison:
        break

    for i in idx_l:

        if 0 < i-idx and i+idx < Max :

            if prison[i+idx]==1:
                prison[i+idx]=0

            if prison[i-idx]==1:
                prison[i-idx]=0

        elif i-idx < 0 and i+idx < Max :
            if prison[i+idx]==1:
                prison[i+idx]=0

        elif 0 < i-idx and Max <= i+idx :
            if prison[i-idx]==1:
                prison[i-idx]=0

    if idx!=0:
        count+=1

    idx+=1

print(count)



