from typing import List


# https://leetcode.cn/problems/minimum-levels-to-gain-more-points/?envType=daily-question&envId=2024-07-19
class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        scores = [1 if i == 1 else -1 for i in possible]
        total_score, score, cnt = sum(scores), 0, 0
        for s in scores:
            score += s
            cnt += 1
            if cnt == len(scores):
                return -1
            if score > total_score - score:
                return cnt
        return cnt


if __name__ == '__main__':
    print(Solution().minimumLevels([1, 0, 1, 0]))
    print(Solution().minimumLevels([1, 1, 1, 1, 1]))
    print(Solution().minimumLevels([0, 0]))
    print(Solution().minimumLevels([1, 1]))
