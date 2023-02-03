def myround(val,digits):
    return round(val+10**(-len(str(val))-1),digits)

n = int(input())

for _ in range(n):
    num, km = input().strip().split(" ")

    if km=="K":
        print(myround(float(num)/1.6,2))
        # print(round(num*1.6,2))
    else:
        print(myround(float(num)*1.6, 2))
        # print(round(num/1.6,2))