from typing import List


# https://leetcode.cn/problems/find-indices-with-index-and-value-difference-i/description/?envType=daily-question&envId=2024-05-25
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # 初始化最小值和最大值的下标
        min_index = 0
        max_index = 0

        # 遍历从indexDifference开始到数组末尾的元素
        for j in range(indexDifference, len(nums)):
            # 计算与当前下标j相隔indexDifference的前一个下标i
            i = j - indexDifference

            # 如果当前元素小于最小值，更新最小值的下标
            if nums[i] < nums[min_index]:
                min_index = i

            # 检查当前元素与最小值的差是否满足条件，如果满足，返回下标对
            if nums[j] - nums[min_index] >= valueDifference:
                return [min_index, j]

            # 如果当前元素大于最大值，更新最大值的下标
            if nums[i] > nums[max_index]:
                max_index = i

            # 检查当前元素与最大值的差是否满足条件，如果满足，返回下标对
            if nums[max_index] - nums[j] >= valueDifference:
                return [max_index, j]

        # 如果遍历结束都没有找到满足条件的下标对，返回[-1, -1]
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.findIndices([5, 1, 4, 1], 2, 4))
    print(s.findIndices([2, 1], 0, 0))
    print(s.findIndices([1, 2, 3], 2, 4))
    print(s.findIndices([2, 29, 0], 0, 12))
    print(s.findIndices([31, 23, 36], 1, 11))
