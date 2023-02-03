import heapq

heap = []
target = []
temp = list(map(int, input().split(" ")))

for i in temp:
    heapq.heappush(heap,i)

while(1<len(heap)):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    target.append(a+b)
    heapq.heappush(heap,a+b)

print(sum(target))

