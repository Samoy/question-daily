from bisect import bisect_right, bisect_left
from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/range-frequency-queries/description/?envType=daily-question&envId=2025-02-18
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        pos = defaultdict(list)
        for i, x in enumerate(arr):
            pos[x].append(i)
        self.pos = pos

    def query(self, left: int, right: int, value: int) -> int:
        a = self.pos[value]
        return bisect_right(a, right) - bisect_left(a, left)


if __name__ == '__main__':
    range_free_query = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
    print(range_free_query.query(1, 2, 4))
    print(range_free_query.query(0, 11, 33))
