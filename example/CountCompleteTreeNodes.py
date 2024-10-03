# Учитывая корень полного двоичного дерева, верните количество узлов в дереве. 
# Согласно Википедии, в полном двоичном дереве каждый уровень, за исключением, возможно, последнего, полностью заполнен,
#  и все узлы на последнем уровне расположены как можно левее. 
# Он может содержать от 1 до 2 в степени n узлов включительно на последнем уровне n. 
# Разработайте алгоритм, который выполняется за время, меньшее, чем O(n).

"""
Input: root = [1,2,3,4,5,6]
Output: 6
"""

class Solution:
    def compute_depth(self, node: TreeNode) -> int:
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d

    def exists(self, idx: int, d: int, node: TreeNode) -> bool:
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None
        
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        d = self.compute_depth(root)
        if d == 0:
            return 1
        
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exists(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        
        return (2**d - 1) + left
    
if __name__ == "__main__":
    example = Solution()
    res = example.countNodes(root = [1,2,3,4,5,6])
    print(res)