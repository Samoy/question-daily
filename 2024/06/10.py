from typing import List


# https://leetcode.cn/problems/boats-to-save-people/?envType=daily-question&envId=2024-06-10
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        cnt = 0
        people.sort()
        i, j = 0, len(people) - 1
        while i <= j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.numRescueBoats([1, 2], 3))
    print(s.numRescueBoats([3, 2, 2, 1], 3))
    print(s.numRescueBoats([3, 5, 3, 4], 5))
    print(s.numRescueBoats([2, 2, 2, 3, 4, 5], 5))
    print(s.numRescueBoats([2, 2], 6))
