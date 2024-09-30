# Дан целочисленный массив nums, верните целочисленный массив counts, 
# где counts[i] - это количество элементов справа от nums[i], которые меньше nums[i].

"""
Input: nums = [5,2,6,1]
Output: [2,1,1,0]
"""

from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def update(index, value, tree, size):
            index += size
            tree[index] += value
            while index > 1:
                index //= 2
                tree[index] = tree[index * 2] + tree[index * 2 + 1]

        def query(left, right, tree, size):
            result = 0
            left += size
            right += size
            while left < right:
                if left % 2 == 1:
                    result += tree[left]
                    left += 1
                left //= 2
                if right % 2 == 1:
                    right -= 1
                    result += tree[right]
                right //= 2
            return result

        offset = 10**4
        size = 2 * 10**4 + 1
        tree = [0] * (2 * size)
        result = []
        for num in reversed(nums):
            smaller_count = query(0, num + offset, tree, size)
            result.append(smaller_count)
            update(num + offset, 1, tree, size)
        return reversed(result)

if __name__ == "__main__":
    example = Solution()
    res = example.countSmaller(nums = [5,2,6,1])
    print(res)