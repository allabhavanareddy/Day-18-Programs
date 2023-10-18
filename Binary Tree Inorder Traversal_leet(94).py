94. Binary Tree Inorder Traversal
Input: root = [1,null,2,3]
Output: [1,3,2]

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def inorder(root):
            if root==None:
                return
            inorder(root.left)
            l.append(root.val)
            inorder(root.right)
        inorder(root)
        return l
        