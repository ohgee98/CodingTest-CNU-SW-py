a = list(map(int,input().strip().split(" ")))
b = list(map(int,input().strip().split(" ")))

union = a+b
print(*set(union))

intersection = []

for i in a:
    if i in b:
        intersection.append(i)

print(*sorted(intersection))

diff = []
for i in a:
    if i not in intersection:
        diff.append(i)

print(*sorted(diff))