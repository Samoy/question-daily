from typing import List


# https://leetcode.cn/problems/replace-elements-with-greatest-element-on-right-side/?envType=daily-question&envId=2025-02-16
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1] * n
        for i in range(n - 2, -1, -1):
            ans[i] = max(ans[i + 1], arr[i + 1])
        return ans


if __name__ == '__main__':
    print(Solution().replaceElements([17, 18, 5, 4, 6, 1]))
    print(Solution().replaceElements([400]))
