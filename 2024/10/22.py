from typing import List


# https://leetcode.cn/problems/count-pairs-that-form-a-complete-day-i/?envType=daily-question&envId=2024-10-22
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        for i in range(len(hours) - 1):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    ans += 1
        return ans


if __name__ == '__main__':
    print(Solution().countCompleteDayPairs([12, 12, 30, 24, 24]))
    print(Solution().countCompleteDayPairs([72, 48, 24, 3]))
