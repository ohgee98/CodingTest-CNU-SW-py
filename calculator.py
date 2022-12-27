str = input().strip()

# 숫자가 n자리일 수 있기 때문에 처리
tokens = []
val = 0
flag = False
for c in str:
    if c.isdigit():
        val = val*10+int(c)
        flag = True

    else:
        if flag:
            tokens.append(val)
            val = 0

        flag=False
        tokens.append(c)

if flag:
    tokens.append(val)

# 후위표기식으로 변경
op = {"*":3,"/":3,"+":2,"-":2,"(":1}
sub = []
postfix = []

for token in tokens:
    if type(token) is int:
        postfix.append(token)

    elif token=="(":
        sub.append(token)

    elif token==")":
        while sub[-1] != "(":
            postfix.append(sub.pop())
        sub.pop()

    else:
        if len(sub)==0:
            sub.append(token)
        else:
            while len(sub) > 0:
                if op[sub[-1]] >= op[token]:
                    postfix.append(sub.pop())
                else:
                    break

            sub.append(token)

while len(sub)>0:
    postfix.append(sub.pop())

# 실제 계산하기
temp = []

for token in postfix:
    if type(token) is int:
        temp.append(token)

    elif token=="+":
        t1 = temp.pop()
        t2 = temp.pop()
        temp.append(t2+t1)
    elif token=="-":
        t1 = temp.pop()
        t2 = temp.pop()
        temp.append(t2-t1)
    elif token=="*":
        t1 = temp.pop()
        t2 = temp.pop()
        temp.append(t2*t1)
    elif token=="/":
        t1 = temp.pop()
        t2 = temp.pop()
        temp.append(int(t2/t1))

print(temp.pop())
