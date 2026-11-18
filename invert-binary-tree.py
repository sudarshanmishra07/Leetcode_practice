class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None                 #if node is empty
        tmp = root.left                 #store left child node temporarily
        root.left = root.right          #move right child to left child
        root.right = tmp                #move stored left child to right
        self.invertTree(root.left)      #invert left subtree
        self.invertTree(root.right)     #invert right subtree
        return root                     