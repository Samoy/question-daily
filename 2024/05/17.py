from typing import List


# https://leetcode.cn/problems/most-profit-assigning-work/description/?envType=daily-question&envId=2024-05-17


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # 先将工作按难度和利润排序，这里默认排序规则是先按难度升序排列，相同难度下按利润降序排列
        jobs = sorted(zip(difficulty, profit), key=lambda x: (x[0], -x[1]))

        # 初始化最大收益为0
        total_profit = 0
        # 初始化工作遍历索引为0
        i = 0
        # 初始化当前最大利润
        max_profit = 0

        # 按照工人能力从小到大排序
        for w in sorted(worker):
            # 遍历工作列表，直到找不到难度小于等于w的工作或者工作列表遍历完
            while i < len(jobs) and w >= jobs[i][0]:
                # 更新最大利润
                max_profit = max(max_profit, jobs[i][1])
                # 移动工作列表索引
                i += 1
            # 为当前工人添加最大利润
            total_profit += max_profit

        # 返回总利润
        return total_profit


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]))
    print(s.maxProfitAssignment([85, 47, 57], [24, 66, 99], [40, 25, 25]))
