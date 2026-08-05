# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Trường hợp 1: Cả hai cây (hoặc 2 nhánh) đều rỗng -> Giống nhau
        if not p and not q:
            return True
        
        # Trường hợp 2: Chỉ có 1 trong 2 cây rỗng (khác cấu trúc)
        # HOẶC giá trị của 2 nút hiện tại khác nhau -> Khác nhau
        if not p or not q or p.val != q.val:
            return False
        
        # Trường hợp 3: Nút hiện tại giống nhau, đi kiểm tra tiếp nhánh trái VÀ nhánh phải
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)