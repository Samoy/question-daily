from typing import List


# https://leetcode.cn/problems/magnetic-force-between-two-balls/?envType=daily-question&envId=2025-02-14
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        def check(x: int) -> bool:
            pre = position[0]
            cnt = 1
            for i in range(1, len(position)):
                if position[i] - pre >= x:
                    pre = position[i]
                    cnt += 1
            return cnt >= m

        position.sort()
        left, right, ans = 1, position[-1] - position[0], -1
        while left <= right:
            mid = (left + right) // 2;
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


if __name__ == '__main__':
    print(Solution().maxDistance(position=[1, 2, 3, 4, 7], m=3))
    print(Solution().maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2))
