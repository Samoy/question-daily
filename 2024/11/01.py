from typing import List


# https://leetcode.cn/problems/maximum-energy-boost-from-two-drinks/?envType=daily-question&envId=2024-11-01
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        # 初始化饮料A，B的最大能量
        prev_A, prev_B = energyDrinkA[0], energyDrinkB[0]
        for i in range(1, len(energyDrinkA)):
            cur_A = max(
                # 继续选择A饮料
                prev_A + energyDrinkA[i],
                # 从A切换到B
                prev_B - energyDrinkB[i - 1] + energyDrinkA[i])
            cur_B = max(
                # 继续选择B饮料
                prev_B + energyDrinkB[i],
                # 从B切换到A饮料
                prev_A - energyDrinkA[i - 1] + energyDrinkB[i]
            )
            prev_A, prev_B = cur_A, cur_B
        return max(prev_A, prev_B)


if __name__ == '__main__':
    print(Solution().maxEnergyBoost(energyDrinkA=[1, 3, 1], energyDrinkB=[3, 1, 1]))
    print(Solution().maxEnergyBoost(energyDrinkA=[4, 1, 1], energyDrinkB=[1, 1, 3]))
