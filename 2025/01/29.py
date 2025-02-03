from typing import List


# https://leetcode.cn/problems/contains-duplicate-ii/?envType=daily-question&envId=2025-01-29
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        st = set()
        for i, x in enumerate(nums):
            if x in st:
                return True
            st.add(x)
            if i >= k:
                st.remove(nums[i - k])
        return False


if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
    print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
    print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))
