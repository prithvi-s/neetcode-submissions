# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        ans = []
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                x = q.popleft()
                if x:
                    level.append(x.val)
                    q.append(x.left)
                    q.append(x.right)
            if level:
                ans.append(level)
        return ans