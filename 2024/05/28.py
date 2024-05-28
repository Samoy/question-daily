from typing import List


# https://leetcode.cn/problems/find-the-peaks/description/?envType=daily-question&envId=2024-05-28
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        ans = []
        i = 1
        while i < len(mountain) - 1:
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                ans.append(i)
                i += 2
            else:
                i += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findPeaks([2, 4, 4]))
    print(s.findPeaks([1, 4, 3, 8, 5]))
