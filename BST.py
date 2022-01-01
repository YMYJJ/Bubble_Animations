from TreeNode import *
class BST():
    def __init__(self, node=None):
        
        node = TreeNode(node)
        self.root_node = node

    def insert(self, x):
    
        
        if self.is_exist(x):#�ж������Ƿ���ڸýڵ�
            return
        p = TreeNode(x)
        if self.root_node == None:#�����Ϊ�յĻ����򽫲���Ľڵ���Ϊ���ڵ�
            self.root_node = p
        else:
            cur = self.root_node
            pre = None
            while cur != None:#���÷ǵݹ�ķ�������
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
    bs_tree = BST(16)   #��ʼ��������
    #�Զ��������������
    bs_tree.insert(9)
    bs_tree.insert(24)
    bs_tree.insert(12)
    bs_tree.insert(6)
    bs_tree.insert(20)
    bs_tree.insert(30)
