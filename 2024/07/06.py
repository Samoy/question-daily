from typing import List


# https://leetcode.cn/problems/count-alternating-subarrays/description/?envType=daily-question&envId=2024-07-06
class Solution:
    """
    给你一个二进制数组nums 。
    如果一个子数组中不存在两个相邻元素的值相同的情况，我们称这样的子数组为交替子数组 。
    返回数组 nums 中交替子数组的数量。
    """

    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0  # 用于累计所有交替子数组的数量
        count = 1  # 当前连续交替序列的长度初始化为1（单个元素也是交替子数组）

        for i in range(1, n):
            # 检查当前元素与前一个元素是否不同
            if nums[i] != nums[i - 1]:
                count += 1  # 相邻不同，增加计数
            else:
                # 遇到相同元素，将当前计数加入结果并重置计数（从当前位置作为新的交替序列开始）
                result += count * (count + 1) // 2  # 使用公式计算并累加当前序列的所有交替子数组数量
                count = 1  # 重置计数，当前元素作为新序列的起点

        # 处理最后一个序列，因为循环结束后不会进入else分支
        result += count * (count + 1) // 2

        return result


if __name__ == '__main__':
    print(Solution().countAlternatingSubarrays([0, 1, 1, 1]))
    print(Solution().countAlternatingSubarrays([1, 0, 1, 0]))
    print(Solution().countAlternatingSubarrays([1, 0, 1, 0, 0]))
