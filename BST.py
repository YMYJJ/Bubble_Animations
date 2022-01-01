from TreeNode import *
class BST():
    def __init__(self, node=None):
        
        node = TreeNode(node)
        self.root_node = node

    def insert(self, x):
    
        
        if self.is_exist(x):#判断树中是否存在该节点
            return
        p = TreeNode(x)
        if self.root_node == None:#如果树为空的话，则将插入的节点置为根节点
            self.root_node = p
        else:
            cur = self.root_node
            pre = None
            while cur != None:#利用非递归的方法遍历
                pre = cur
                if cur.val < x:
                    cur = cur.right
                else:
                    cur = cur.left

            p.parent = pre
            if pre.val < x:
                pre.right = p
            else:
                pre.left = p

    def is_exist(self, k):

        cur = self.root_node
        while cur != None and cur.val != k:
            if k < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return True if cur != None else False

if __name__ == '__main__':
    bs_tree = BST(16)   #初始化二叉树
    #对二叉树做插入操作
    bs_tree.insert(9)
    bs_tree.insert(24)
    bs_tree.insert(12)
    bs_tree.insert(6)
    bs_tree.insert(20)
    bs_tree.insert(30)
