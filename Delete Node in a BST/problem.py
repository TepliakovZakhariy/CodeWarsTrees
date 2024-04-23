# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val<key:
            root.right= self.deleteNode(root.right,key)
        elif root.val>key:
            root.left= self.deleteNode(root.left,key)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                if abs(root.val-root.left.val)<abs(root.val-root.right.val):
                    changed_root=root.left
                    while changed_root.right:
                        changed_root=changed_root.right
                    root.val=changed_root.val
                    root.left=self.deleteNode(root.left,changed_root.val)
                else:
                    changed_root=root.right
                    while changed_root.left:
                        changed_root=changed_root.left
                    root.val=changed_root.val
                    root.right=self.deleteNode(root.right,changed_root.val)
        return root
