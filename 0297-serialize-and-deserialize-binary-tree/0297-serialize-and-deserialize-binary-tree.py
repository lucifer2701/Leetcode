# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if not root:
            return 'null'
        return str(root.val)+','+str(self.serialize(root.left))+','+str(self.serialize(root.right))
        
    def deserialize(self, data):
        data=list(data.split(','))
        def dfs(data_list):
            root=data_list.pop(0)
            if root=='null':
                return None
            root=TreeNode(int(root))
            root.left=dfs(data_list)
            root.right=dfs(data_list)
            return root
        return dfs(data)
       
        
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))