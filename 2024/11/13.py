from typing import List


# https://leetcode.cn/problems/count-substrings-that-satisfy-k-constraint-ii/?envType=daily-question&envId=2024-11-13
class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        right = [n] * n
        pre = [0] * (n + 1)
        cnt = [0, 0]
        l = 0
        for i, c in enumerate(s):
            cnt[ord(c) & 1] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[l]) & 1] -= 1
                right[l] = i
                l += 1
            pre[i + 1] = pre[i] + i - l + 1

        ans = []
        for l, r in queries:
            j = min(right[l], r + 1)
            ans.append(pre[r + 1] - pre[j] + (j - l + 1) * (j - l) // 2)
        return ans


if __name__ == '__main__':
    print(Solution().countKConstraintSubstrings(s="0001111", k=2, queries=[[0, 6]]))
    print(Solution().countKConstraintSubstrings(s="010101", k=1, queries=[[0, 5], [1, 4], [2, 3]]))
