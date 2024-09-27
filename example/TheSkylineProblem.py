
"""
Горизонт города — это внешний контур силуэта, образованного всеми зданиями в этом городе, когда они видны издалека. Учитывая расположения и высоты всех зданий, верните горизонт, образованный этими зданиями в совокупности.
Геометрическая информация о каждом здании задана в массиве buildings, где buildings[i] = [lefti, righti, heighti]:
lefti — это координата x левого края i-го здания.
righti — это координата x правого края i-го здания.
heighti — это высота i-го здания.
Вы можете предположить, что все здания — это идеальные прямоугольники, стоящие на абсолютно плоской поверхности на высоте 0.
"""

"""
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
"""

from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        positions = sorted(list(set([x for building in buildings for x in building[:2]])))
        
        edge_index_map = {x : i for i, x in enumerate(positions)}

        heights = [0] * len(positions)
        
        for left, right, height in buildings:
            left_idx = edge_index_map[left]
            right_idx = edge_index_map[right]

            for i in range(left_idx, right_idx):
                heights[i] = max(heights[i], height)

        answer = []

        for i in range(len(heights)):
            curr_height = heights[i]
            curr_x = positions[i]

            if not answer or answer[-1][1] != curr_height:
                answer.append([curr_x, curr_height])
        return answer

if __name__ == "__main__":
    example = Solution()
    res = example.getSkyline(buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]])
    print(res)