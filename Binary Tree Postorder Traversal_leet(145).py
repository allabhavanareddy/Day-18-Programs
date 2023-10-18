145. Binary Tree Postorder Traversal
Input: root = [1,null,2,3]
Output: [3,2,1]
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def postorder(root):
            if root==None:
                return
           
            postorder(root.left)
            postorder(root.right)
            l.append(root.val)
           
        postorder(root)
        return l
        