from collections import deque

def sq_queue(data, action, temp):
    if action == 0:
        print(len(data))
    elif action == 1:
        t = data.popleft()
        print(t)
        data.appendleft(t)
    elif action == 2:
        data.popleft()
    else:
        data.append(temp)

    return data

def sq_stack(data, action, temp):
    if action == 0:
        print(len(data))
    elif action == 1:
        t = data.pop()
        print(t)
        data.append(t)
    elif action == 2:
        data.pop()
    else:
        data.append(temp)

    return data


sq, n = input().strip().split(" ")
n = int(n)
data = deque()

for _ in range(n):
    check = input().strip()
    if len(check) == 1:
        action = int(check)
        temp = 0
    else:
        action, temp = map(int, check.split(" "))

    if sq == 'Stack':
        data = sq_stack(data, action, temp)
    else:
        data = sq_queue(data, action, temp)