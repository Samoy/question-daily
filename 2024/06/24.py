from typing import List


# https://leetcode.cn/problems/next-greater-element-ii/?envType=daily-question&envId=2024-06-24
class Solution:
    """
    给定一个循环数组 nums （ nums[nums.length - 1] 的下一个元素是 nums[0] ），返回 nums 中每个元素的 下一个更大元素 。
    数字 x 的 下一个更大的元素 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
    如果不存在，则输出 -1 。
    """

    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n  # 初始化结果列表，默认值为 -1
        stack = []  # 使用双端队列作为单调栈，存储待处理元素的索引

        # 遍历扩展后的循环数组，仅需遍历原数组长度即可，因数组已扩展
        for i in range(2 * n):
            # 当栈不为空且当前元素大于栈顶元素对应的值时
            while stack and nums[i % n] > nums[stack[-1]]:
                # 弹出栈顶索引，更新答案列表中该位置的值
                index = stack.pop()
                ans[index] = nums[i % n]
            # 将当前索引入栈，等待后续可能的更大元素
            stack.append(i % n)

        return ans


if __name__ == '__main__':
    print(Solution().nextGreaterElements([1, 2, 1]))
    print(Solution().nextGreaterElements([1, 2, 3, 4, 3]))
