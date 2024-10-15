from itertools import count


# https://leetcode.cn/problems/maximum-height-of-a-triangle/submissions/572798473/?envType=daily-question&envId=2024-10-15
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        cnt = [0, 0]
        for i in count(1):
            cnt[i % 2] += i
            if (cnt[0] > red or cnt[1] > blue) and (cnt[0] > blue or cnt[1] > red):
                return i - 1


if __name__ == '__main__':
    print(Solution().maxHeightOfTriangle(2, 4))
    print(Solution().maxHeightOfTriangle(2, 1))
    print(Solution().maxHeightOfTriangle(1, 1))
    print(Solution().maxHeightOfTriangle(10, 1))
