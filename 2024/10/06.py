from typing import List


# https://leetcode.cn/problems/gas-station/?envType=daily-question&envId=2024-10-06
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = min_s = s = 0  # s 表示油量，min_s 表示最小油量
        for i, (g, c) in enumerate(zip(gas, cost)):
            s += g - c  # 在 i 处加油，然后从 i 到 i+1
            if s < min_s:
                min_s = s  # 更新最小油量
                ans = i + 1  # 注意 s 减去 c 之后，汽车在 i+1 而不是 i
        # 循环结束后，s 即为 gas 之和减去 cost 之和
        return -1 if s < 0 else ans


if __name__ == '__main__':
    print(Solution().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
    print(Solution().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
