from typing import List


# https://leetcode.cn/problems/find-indices-of-stable-mountains/?envType=daily-question&envId=2024-12-19
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        ans = []
        for i in range(1, len(height)):
            left = height[i - 1]
            if left > threshold:
                ans.append(i)
        return ans


if __name__ == '__main__':
    print(Solution().stableMountains(height=[1, 2, 3, 4, 5], threshold=2))
    print(Solution().stableMountains(height=[10, 1, 10, 1, 10], threshold=3))
    print(Solution().stableMountains(height=[10, 1, 10, 1, 10], threshold=10))
