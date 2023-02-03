a = {}
b = {}
add = {}
diff = {}

tempA = list(map(int,input().strip().split(" ")))
tempB = list(map(int,input().strip().split(" ")))

i = len(tempA)-1
j = len(tempB)-1

while(0<i):
    a[tempA[i]]=tempA[i-1]
    i-=2

while(0<j):
    b[tempB[j]]=tempB[j-1]
    j-=2

# A+B / A-B
for i in a:
    if i in b:
        add[i]=a[i]+b[i]
        diff[i]=a[i]-b[i]

for i in a:
    if i not in b:
        add[i]=a[i]
        diff[i]=a[i]

for i in b:
    if i not in a:
        add[i]=b[i]
        diff[i]=b[i]

add = sorted(add.items(),reverse=True)
diff = sorted(diff.items(),reverse=True)

for i in add:
    print(i[1], end=' ')
    print(i[0], end=' ')
print()
for i in diff:
    if i[1]==0:
        continue
    print(i[1], end=' ')
    print(i[0], end=' ')
