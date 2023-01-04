
def postorder(root):
    if root != ".":
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end=" ")


n = int(input().strip())
tree = {}
check = {}
root = ""

for i in range(n):
    parent, left, right = input().strip().split(" ")
    tree[parent] = [left, right]

    if i == 0:
        root = parent

postorder(root)
