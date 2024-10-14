from itertools import count


# https://leetcode.cn/problems/super-egg-drop/?envType=daily-question&envId=2024-10-14
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        f = [0] * (k + 1)
        for i in count(1):  # 从 1 开始枚举 i
            for j in range(k, 0, -1):
                f[j] += f[j - 1] + 1
            if f[k] >= n:
                return i


if __name__ == '__main__':
    print(Solution().superEggDrop(1, 2))
    print(Solution().superEggDrop(2, 6))
    print(Solution().superEggDrop(3, 14))
