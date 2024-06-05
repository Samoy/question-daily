from typing import List
from sortedcontainers import SortedList


# https://leetcode.cn/problems/distribute-elements-into-two-arrays-ii/description/?envType=daily-question&envId=2024-06-05

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # 初始化两个有序列表 lst1 和 lst2，以及对应的数组 arr1 和 arr2
        lst1 = SortedList([nums[0]])  # 使用 SortedList 保持元素排序并允许快速查找
        lst2 = SortedList([nums[1]])
        arr1 = [nums[0]]  # 实际存放元素的数组
        arr2 = [nums[1]]

        # 遍历 nums 中剩余的元素
        for num in nums[2:]:
            # 计算 num 在 lst1 和 lst2 中严格大于它的元素数量
            cnt1 = len(lst1) - lst1.bisect_right(num)  # bisect_right 返回第一个大于num的位置，故用总长减去该位置得到大于num的元素数量
            cnt2 = len(lst2) - lst2.bisect_right(num)

            # 根据条件将 num 分配给 lst1 或 lst2
            if cnt1 > cnt2 or (
                    cnt1 == cnt2 and len(lst1) <= len(lst2)):  # 如果 lst1 中大于 num 的元素多，或两者相等但 lst1 短，则 num 加入 lst1
                lst1.add(num)
                arr1.append(num)
            else:  # 否则，num 加入 lst2
                lst2.add(num)
                arr2.append(num)

        # 最后，将 arr1 和 arr2 连接成结果数组并返回
        return arr1 + arr2


if __name__ == '__main__':
    s = Solution()
    print(s.resultArray([2, 1, 3, 3]))
    print(s.resultArray([5, 14, 3, 1, 2]))
    print(s.resultArray([3, 3, 3, 3]))
