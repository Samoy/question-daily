from typing import List


# https://leetcode.cn/problems/alternating-groups-ii/?envType=daily-question&envId=2024-11-27
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans = cnt = 0
        for i in range(n * 2):
            if i > 0 and colors[i % n] == colors[(i - 1) % n]:
                cnt = 0
            cnt += 1
            if i >= n and cnt >= k:
                ans += 1
        return ans


if __name__ == '__main__':
    print(Solution().numberOfAlternatingGroups(colors=[0, 1, 0, 1, 0], k=3))
    print(Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], k=6))
