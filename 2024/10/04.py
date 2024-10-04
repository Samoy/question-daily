# https://leetcode.cn/problems/airplane-seat-assignment-probability/?envType=daily-question&envId=2024-10-04
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 0.5 if n > 1 else 1


if __name__ == '__main__':
    print(Solution().nthPersonGetsNthSeat(1))
    print(Solution().nthPersonGetsNthSeat(2))
