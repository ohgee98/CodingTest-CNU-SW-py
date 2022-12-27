def isEmpty(front, rear, cq):
    if all(i == -1 for i in cq):
        return True
    else:
        return False


def isFull(front, rear, cq):
    if all(i != -1 for i in cq):
        return True
    else:
        return False


from collections import deque

k = int(input())
cq = deque(-1 for _ in range(k))
front = 0
rear = 0

while (True):
    try:
        action = input().strip()
        if 7 < len(action):
            action, n = action.split(" ")

        if action == "enQueue":
            if isFull(front, rear, cq):
                print("false")
            else:
                cq[rear% k] = n
                rear+=1
                # rear = (rear + 1) % k
                print("true")
        elif action == "deQueue":
            if isEmpty(front, rear, cq):
                print("false")
            else:
                cq[front% k] = -1
                front+=1
                # front = (front + 1) % k
                print("true")
        elif action == "Front":
            print(front + 1)
        elif action == "Rear":
            print(rear + 1)
        elif action == "isEmpty":
            if isEmpty(front, rear, cq):
                print("true")
            else:
                print("false")
        elif action == "isFull":
            if isFull(front, rear, cq):
                print("true")
            else:
                print("false")

    except:
        break




