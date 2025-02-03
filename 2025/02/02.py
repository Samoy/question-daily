from typing import List


# https://leetcode.cn/problems/range-addition-ii/?envType=daily-question&envId=2025-02-02
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_a = min((op[0] for op in ops), default=m)
        min_b = min((op[1] for op in ops), default=n)
        return min_a * min_b


if __name__ == '__main__':
    print(Solution().maxCount(3, 3, [[2, 2], [3, 3]]))
    print(Solution().maxCount(3, 3, [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3],
                                     [3, 3], [3, 3]]))
    print(Solution().maxCount(3, 3, []))
