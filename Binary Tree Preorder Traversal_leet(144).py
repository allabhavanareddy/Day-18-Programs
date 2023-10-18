144. Binary Tree Preorder Traversal
Input: root = [1,null,2,3]
Output: [1,2,3]

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        l=[]
        def preorder(root):
            if root==None:
                return
            l.append(root.val)
            preorder(root.left)
            preorder(root.right)
           
        preorder(root)
        return l