def preorder(root):
    if root != ".":
        print(root, end=" ")
        if root in tree:
            preorder(tree[root][0])
            preorder(tree[root][1])


def inorder(root):
    if root != ".":
        if root in tree:
            inorder(tree[root][0])

        print(root, end=" ")

        if root in tree:
            inorder(tree[root][1])


def postorder(root):
    if root != ".":
        if root in tree:
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


preorder(root)
print()
inorder(root)
print()
postorder(root)
