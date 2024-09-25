from collections import defaultdict
from itertools import combinations
from typing import List


# https://leetcode.cn/problems/naming-a-company/?envType=daily-question&envId=2024-09-25
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = defaultdict(set)
        for s in ideas:
            groups[s[0]].add(s[1:])
        ans = 0
        for a, b in combinations(groups.values(), 2):
            m = len(a & b)
            ans += (len(a) - m) * (len(b) - m)
        return ans * 2


if __name__ == '__main__':
    print(Solution().distinctNames(["coffee", "donuts", "time", "toffee"]))
    print(Solution().distinctNames(["lack", "back"]))
