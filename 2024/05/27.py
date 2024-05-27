from typing import List


# https://leetcode.cn/problems/find-missing-observations/?envType=daily-question&envId=2024-05-27
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # 有记录次数
        m = len(rolls)
        # 总次数
        times = m + n
        # 总和
        total = mean * times
        # 剩余和
        remain = total - sum(rolls)
        # 接下来的问题就是如何使用n个元素(1~6)的和凑成remain
        # 如果remain/n > 6 ，则说明凑不够，因此直接返回[]
        if remain / n > 6 or remain / n < 1:
            return []
        # 使用平均值填充数组
        ave = int(remain / n)
        ans = [ave] * n
        # 数值不够，使用取模补充
        mod = remain % n
        if mod > 0:
            for i in range(mod):
                ans[i] = ans[i] + 1
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.missingRolls([3, 2, 4, 3], 4, 2))
    print(s.missingRolls([1, 5, 6], 3, 4))
    print(s.missingRolls([1, 2, 3, 4], 6, 4))
    print(s.missingRolls([1], 3, 1))
