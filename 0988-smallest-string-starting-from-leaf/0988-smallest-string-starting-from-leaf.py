class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, current_string):
            current_string = chr(ord("a") + node.val) + current_string
            if not (node.left or node.right):
                return current_string
            res = chr(ord("a") + 27)
            if node.left:
                res = min(res, dfs(node.left, current_string))
            if node.right:
                res = min(res, dfs(node.right, current_string))
            return res
            
        return dfs(root, "")