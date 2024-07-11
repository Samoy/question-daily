from typing import List


# https://leetcode.cn/problems/count-the-number-of-incremovable-subarrays-ii/description/?envType=daily-question&envId=2024-07-11
class Solution:
    def incremovableSubarrayCount(self, a: List[int]) -> int:
        n = len(a)
        i = 0
        while i < n - 1 and a[i] < a[i + 1]:
            i += 1
        if i == n - 1:  # 每个非空子数组都可以移除
            return n * (n + 1) // 2

        ans = i + 2  # 不保留后缀的情况，一共 i+2 个
        # 枚举保留的后缀为 a[j:]
        j = n - 1
        while j == n - 1 or a[j] < a[j + 1]:
            while i >= 0 and a[i] >= a[j]:
                i -= 1
            # 可以保留前缀 a[:i+1], a[:i], ..., a[:0] 一共 i+2 个
            ans += i + 2
            j -= 1
        return ans


if __name__ == '__main__':
    print(Solution().incremovableSubarrayCount([1, 2, 3, 4]))
    print(Solution().incremovableSubarrayCount([6, 5, 7, 8]))
    print(Solution().incremovableSubarrayCount([8, 7, 6, 6]))
