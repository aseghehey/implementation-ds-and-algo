class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def insert_to_left(self, child):
        if self.left is None:
            self.left = TreeNode(child)
        else:
            child = TreeNode(child)
            child.left = self.left
            self.left = child
            
    def insert_to_right(self, child):
        if self.right is None:
            self.right = TreeNode(child)
        else:
            child = TreeNode(child)
            child.right = self.right
            self.right = child
    
tree = TreeNode('E')
tree.insert_to_left('M')
tree.insert_to_right('A')
tree.insert_to_left('P')
