from typing import List


# https://leetcode.cn/problems/find-the-most-competitive-subsequence/description/?envType=daily-question&envId=2024-05-25
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        # 初始化结果列表
        ans = []

        # 遍历输入数组nums
        for i, num in enumerate(nums):
            # 当结果列表非空，且最后一个元素大于当前元素，同时满足条件（当前索引与数组末尾的距离加上结果列表长度大于等于k）
            # 这意味着可以通过移除结果列表末尾的元素来使子序列更具竞争力
            while ans and ans[-1] > num and len(ans) - 1 + len(nums) - i >= k:
                # 移除结果列表的最后一个元素
                ans.pop()

            # 如果结果列表长度小于k，说明还可以添加元素，将当前元素添加到结果列表
            if len(ans) < k:
                ans.append(num)

        # 返回最终的竞争性子序列
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.mostCompetitive(nums=[3, 5, 2, 6], k=2))
    print(s.mostCompetitive(nums=[2, 4, 3, 3, 5, 4, 9, 6], k=4))
