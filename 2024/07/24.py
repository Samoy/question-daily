from typing import List


# https://leetcode.cn/problems/relocate-marbles/description/?envType=daily-question&envId=2024-07-24
class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        st = set(nums)
        for f, t in zip(moveFrom, moveTo):
            st.remove(f)
            st.add(t)
        return sorted(st)


if __name__ == '__main__':
    print(Solution().relocateMarbles(nums=[1, 6, 7, 8], moveFrom=[1, 7, 2], moveTo=[2, 9, 5]))
    print(Solution().relocateMarbles(nums=[1, 1, 3, 3], moveFrom=[1, 3], moveTo=[2, 2]))
