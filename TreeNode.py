class TreeNode():
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.val)
