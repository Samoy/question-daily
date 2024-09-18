from typing import List


# https://leetcode.cn/problems/the-latest-time-to-catch-a-bus/?envType=daily-question&envId=2024-09-18
class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        c: int = 0

        # 模拟乘客上车
        j = 0
        for t in buses:
            c = capacity
            while c and j < len(passengers) and passengers[j] <= t:
                j += 1
                c -= 1
        # 寻找插队时机
        j -= 1
        ans = buses[-1] if c else passengers[j]
        while j >= 0 and ans == passengers[j]:
            ans -= 1
            j -= 1
        return ans


if __name__ == '__main__':
    print(Solution().latestTimeCatchTheBus(buses=[10, 20], passengers=[2, 17, 18, 19], capacity=2))
    print(Solution().latestTimeCatchTheBus(buses=[20, 30, 10], passengers=[19, 13, 26, 4, 25, 11, 21], capacity=2))
