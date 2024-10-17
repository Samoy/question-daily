from typing import List


# https://leetcode.cn/problems/count-the-number-of-inversions/?envType=daily-question&envId=2024-10-17
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 1_000_000_007
        req = [-1] * n
        req[0] = 0
        for end, cnt in requirements:
            req[end] = cnt
        if req[0]:
            return 0

        m = max(req)
        f = [0] * (m + 1)
        f[0] = 1
        for i in range(1, n):
            mx = m if req[i] < 0 else req[i]
            r = req[i - 1]
            if r >= 0:
                for j in range(m + 1):
                    f[j] = f[r] if r <= j <= min(i + r, mx) else 0
            else:
                for j in range(1, mx + 1):  # 计算前缀和
                    f[j] = (f[j] + f[j - 1]) % MOD
                for j in range(mx, i, -1):  # 计算子数组和
                    f[j] = (f[j] - f[j - i - 1]) % MOD
        return f[req[-1]]


if __name__ == '__main__':
    print(Solution().numberOfPermutations(n=3, requirements=[[2, 2], [0, 0]]))
    print(Solution().numberOfPermutations(n=3, requirements=[[2, 2], [1, 1], [0, 0]]))
