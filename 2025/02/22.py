from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/count-pairs-of-similar-strings/?envType=daily-question&envId=2025-02-22
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        cnt = defaultdict(int)
        for s in words:
            mask = 0
            for c in s:
                mask |= 1 << (ord(c) - ord('a'))
            ans += cnt[mask]
            cnt[mask] += 1
        return ans


if __name__ == '__main__':
    print(Solution().similarPairs(["aba", "aabb", "abcd", "bac", "aabc"]))
    print(Solution().similarPairs(["aabb", "ab", "ba"]))
    print(Solution().similarPairs(["nba", "cba", "dba"]))
