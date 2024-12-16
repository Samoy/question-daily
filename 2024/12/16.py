from cmath import inf
from typing import List

from sortedcontainers import SortedList


# https://leetcode.cn/problems/closest-room/?envType=daily-question&envId=2024-12-16
class Solution:
    def closestRoom(
            self, rooms: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        rooms.sort(key=lambda r: r[1])  # 按照 size 从小到大排序
        q = len(queries)
        ans = [-1] * q
        room_ids = SortedList()
        j = len(rooms) - 1
        for i in sorted(
                range(q), key=lambda i: -queries[i][1]
        ):  # 按照 minSize 从大到小排序
            preferred_id, min_size = queries[i]
            while j >= 0 and rooms[j][1] >= min_size:
                room_ids.add(rooms[j][0])
                j -= 1

            diff = inf
            k = room_ids.bisect_left(preferred_id)
            if k:
                diff = preferred_id - room_ids[k - 1]  # 左边的差
                ans[i] = room_ids[k - 1]
            if k < len(room_ids) and room_ids[k] - preferred_id < diff:  # 右边的差更小
                ans[i] = room_ids[k]
        return ans


if __name__ == '__main__':
    print(Solution().closestRoom(rooms=[[2, 2], [1, 2], [3, 2]], queries=[[3, 1], [3, 3], [5, 2]]))
    print(Solution().closestRoom(rooms=[[1, 4], [2, 3], [3, 5], [4, 1], [5, 2]], queries=[[2, 3], [2, 4], [2, 5]]))
