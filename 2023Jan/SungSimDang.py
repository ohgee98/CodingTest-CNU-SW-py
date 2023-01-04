aName = input().strip()
aPrice = int(input())
bName = input().strip()
bPrice = int(input())

if aPrice < bPrice:
    print(bName)
else:
    print(aName)