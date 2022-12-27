import re

arr = ""
while True:
    try:
        line = input().lower().strip()
        arr = arr + " " + line
    except EOFError:
        break

a = arr.strip()
a = re.sub(r"\s+"," ", a)
a = a.split(" ")

total_char = len(a)
list_a = set(a)
most_char = ""
most_char_num = 0

for i in list_a:
    temp = a.count(i)

    if most_char_num < temp:
        most_char_num = temp
        most_char = i

print(most_char, round(most_char_num / total_char, 2))
