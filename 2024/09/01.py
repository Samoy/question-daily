from typing import List


# https://leetcode.cn/problems/number-of-students-doing-homework-at-a-given-time/description/?envType=daily-question&envId=2024-09-01
class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum(s <= queryTime <= e for s, e in zip(startTime, endTime))


if __name__ == '__main__':
    print(Solution().busyStudent([1, 2, 3], [3, 2, 7], 4))
    print(Solution().busyStudent([4], [4], 4))
    print(Solution().busyStudent([4], [4], 5))
    print(Solution().busyStudent([1, 1, 1, 1], [1, 3, 2, 4], 7))
    print(Solution().busyStudent([9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10], 5))
