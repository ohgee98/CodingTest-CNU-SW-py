def fibo(temp):
    if temp == 1:
        return 1
    elif temp == 0:
        return 0
    else:
        return fibo(temp - 1) + fibo(temp - 2)


a = int(input())
print(fibo(a))