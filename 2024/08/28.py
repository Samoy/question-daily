from collections import defaultdict
from math import inf


# https://leetcode.cn/problems/minimum-substring-partition-of-equal-character-frequency/?envType=daily-question&envId=2024-08-28
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)
        f = [0] + [inf] * n
        for i in range(n):
            cnt = defaultdict(int)
            max_cnt = 0
            for j in range(i, -1, -1):
                cnt[s[j]] += 1
                max_cnt = max(max_cnt, cnt[s[j]])
                if i - j + 1 == len(cnt) * max_cnt:
                    f[i + 1] = min(f[i + 1], f[j] + 1)
        return f[n]


if __name__ == '__main__':
    print(Solution().minimumSubstringsInPartition("fabccddg"))
    print(Solution().minimumSubstringsInPartition("abababaccddb"))
