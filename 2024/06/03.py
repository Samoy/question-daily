from typing import List


# https://leetcode.cn/problems/distribute-candies-to-people/description/?envType=daily-question&envId=2024-06-03
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i = 0
        while candies != 0:
            ans[i % num_people] += min(i + 1, candies)
            candies -= min(i + 1, candies)
            i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies(7, 4))
    print(s.distributeCandies(10, 3))
