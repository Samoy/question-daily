from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/destination-city/?envType=daily-question&envId=2024-10-08
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = defaultdict(int)
        for path in paths:
            d[path[0]] += 1
            d[path[1]] += 0
        for key in d:
            if d[key] == 0:
                return key
        return ""


if __name__ == '__main__':
    print(Solution().destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
    print(Solution().destCity([["B", "C"], ["D", "B"], ["C", "A"]]))
    print(Solution().destCity([["A", "Z"]]))
