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
        def dfs(d_list):
            node=d_list.pop(0)
            if node=='null':    return None
            node=TreeNode(node)
            node.left=dfs(d_list)
            node.right=dfs(d_list)
            return node
        return dfs(data)
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))