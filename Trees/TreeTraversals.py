def bfs(root):
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.val)
            queue.append(root.left)
            queue.append(root.right)

# ---------------------- DFS ------------------------------------------ #

def dfs(root):
    if root:
        dfs(root.left)
        dfs(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
