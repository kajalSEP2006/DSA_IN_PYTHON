"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):

        if not root:
             return []
        ans = []
        q = [root]
        while q:
                level_size = len(q)
                level = []
                next_q = []
                for i in range(level_size):
                  node = q[i]
                  level.append(node.val)   
                  for child in node.children:
                    next_q.append(child)
                ans.append(level)
                q = next_q    

        return ans



            
       
        