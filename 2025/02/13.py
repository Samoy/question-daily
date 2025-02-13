from collections import Counter


# https://leetcode.cn/problems/maximum-number-of-balls-in-a-box/?envType=daily-question&envId=2025-02-13
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        count = Counter(sum(map(int, str(i))) for i in range(lowLimit, highLimit + 1))
        return max(count.values())


if __name__ == '__main__':
    print(Solution().countBalls(1, 10))
    print(Solution().countBalls(5, 15))
    print(Solution().countBalls(19, 28))
