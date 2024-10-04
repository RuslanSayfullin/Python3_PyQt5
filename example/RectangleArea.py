# Даны координаты двух прямоугольных прямоугольников на двумерной плоскости, верните общую площадь, покрытую этими двумя прямоугольниками. 
# Первый прямоугольник определяется его нижним левым углом (ax1, ay1) и верхним правым углом (ax2, ay2). 
# Второй прямоугольник определяется его нижним левым углом (bx1, by1) и верхним правым углом (bx2, by2).

"""
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45
"""

class Solution:
    def computeArea(self,
                    ax1: int, ay1: int,
                    ax2: int, ay2: int,
                    bx1: int, by1: int,
                    bx2: int, by2: int) -> int:
        area_of_a = (ay2 - ay1) * (ax2 - ax1)
        area_of_b = (by2 - by1) * (bx2 - bx1)

        left = max(ax1, bx1)
        right = min(ax2, bx2)
        x_overlap = right - left

        top = min(ay2, by2)
        bottom = max(ay1, by1)
        y_overlap = top - bottom

        area_of_overlap = 0
        if x_overlap > 0 and y_overlap > 0:
            area_of_overlap = x_overlap * y_overlap

        total_area = area_of_a + area_of_b - area_of_overlap

        return total_area
    
if __name__ == "__main__":
    example = Solution()
    res = example.computeArea(ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2)
    print(res)    