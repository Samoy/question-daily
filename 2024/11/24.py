from heapq import heapify, heapreplace
from typing import List


# https://leetcode.cn/problems/smallest-range-covering-elements-from-k-lists/?envType=daily-question&envId=2024-11-24
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 把每个列表的第一个元素入堆
        h = [(arr[0], i, 0) for i, arr in enumerate(nums)]
        heapify(h)

        ans_l = h[0][0]  # 第一个合法区间的左端点
        ans_r = r = max(arr[0] for arr in nums)  # 第一个合法区间的右端点
        while h[0][2] + 1 < len(nums[h[0][1]]):  # 堆顶列表有下一个元素
            _, i, j = h[0]
            x = nums[i][j + 1]  # 堆顶列表的下一个元素
            heapreplace(h, (x, i, j + 1))  # 替换堆顶
            r = max(r, x)  # 更新合法区间的右端点
            l = h[0][0]  # 当前合法区间的左端点
            if r - l < ans_r - ans_l:
                ans_l, ans_r = l, r
        return [ans_l, ans_r]


if __name__ == '__main__':
    print(Solution().smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]))
    print(Solution().smallestRange([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
