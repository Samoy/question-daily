from typing import List


# https://leetcode.cn/problems/alternating-groups-i/?envType=daily-question&envId=2024-11-26
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        cnt = 0
        for i in range(1, len(colors) - 1):
            if colors[i] != colors[i - 1] and colors[i] != colors[i + 1]:
                cnt += 1
        # 计算第一个
        if colors[0] != colors[1] and colors[0] != colors[-1]:
            cnt += 1
        # 计算最后一个
        if colors[-1] != colors[-2] and colors[-1] != colors[0]:
            cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().numberOfAlternatingGroups([1, 1, 1]))
    print(Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1]))
