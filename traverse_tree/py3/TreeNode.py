from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = []
        queue = deque([root])
        while any(queue):
            node = queue.popleft()
            if node is None:
                ret.append("null")
                continue
            ret.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        return ",".join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(data[0])
        queue = deque([(root, 0)])
        while queue:
            node, index = queue.popleft()
            ileft, iright = index * 2 + 1, index * 2 + 2
            if ileft < len(data) and data != "null":
                node.left = TreeNode(data[ileft]) 
                queue.append((node.left, ileft))
            if iright < len(data) and data != "null":
                node.right = TreeNode(data[iright])
                queue.append((node.right, iright))
        return root
