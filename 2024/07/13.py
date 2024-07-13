from typing import List


# https://leetcode.cn/problems/find-if-array-can-be-sorted/?envType=daily-question&envId=2024-07-13
class Solution:
    """
    给你一个下标从 0 开始且全是 正 整数的数组 nums 。
    一次 操作 中，如果两个 相邻 元素在二进制下数位为 1 的数目 相同 ，那么你可以将这两个元素交换。你可以执行这个操作 任意次 （也可以 0 次）。
    如果你可以使数组变有序，请你返回 true ，否则返回 false 。
    """

    def canSortArray(self, nums: List[int]) -> bool:
        # 分段：将数组拆分为多个段。每个段都包含具有相同设置位数的连续元素。
        arr, one_cnt, = [], -1
        for num in nums:
            cnt = bin(num).count('1')
            if cnt != one_cnt:
                one_cnt = cnt
                arr.append([num])
            else:
                arr[-1].append(num)
        # 遍历：从左到右，前一个段的最大元素应小于当前段的最小元素。
        for i in range(1, len(arr)):
            max_before = max(arr[i - 1])
            min_current = min(arr[i])
            if max_before > min_current:
                return False
        return True


if __name__ == '__main__':
    print(Solution().canSortArray([8, 4, 2, 30, 15]))
    print(Solution().canSortArray([1, 2, 3, 4, 5]))
    print(Solution().canSortArray([3, 16, 8, 4, 2]))
