from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/rank-teams-by-votes/?envType=daily-question&envId=2024-12-29
class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        m = len(votes[0])
        cnts = defaultdict(lambda: [0] * m)
        for vote in votes:
            for i, ch in enumerate(vote):
                cnts[ch][i] -= 1  # 改成负数（相反数），方便比大小
        return "".join(sorted(cnts, key=lambda ch: (cnts[ch], ch)))


if __name__ == '__main__':
    print(Solution().rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))
    print(Solution().rankTeams(["WXYZ", "XYZW"]))
