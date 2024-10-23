from typing import List


# https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-ii/description/?envType=daily-question&envId=2024-10-23
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        # 初始化一个长度为24的计数数组，用于记录每个小时数模24后的余数的出现次数
        cnt = [0] * 24
        for h in hours:
            # 对于每个小时数，计算与之匹配的小时数的余数，以找到能组成24小时倍数的对
            # 通过累加对应余数的计数，来统计完整天数的对数
            ans += cnt[(24 - h % 24) % 24]
            # 更新当前小时数余数的计数
            cnt[h % 24] += 1
        # 返回累加的完整天数的对数
        return ans


if __name__ == '__main__':
    print(Solution().countCompleteDayPairs([12, 12, 30, 24, 24]))
    print(Solution().countCompleteDayPairs([72, 48, 24, 3]))
    print(Solution().countCompleteDayPairs([13, 11, 24, 12]))
