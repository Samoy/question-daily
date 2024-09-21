from typing import List


# https://leetcode.cn/problems/find-the-town-judge/?envType=daily-question&envId=2024-09-22
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 初始化信任映射，长度为 n + 1，用于记录每个人的信任状态
        trust_map = [0] * (n + 1)
        # 更新信任状态
        for a, b in trust:
            # a 信任 b，a 的信任值减一
            trust_map[a] -= 1
            # b 被 a 信任，b 的信任值加一
            trust_map[b] += 1
        # 查找法官
        for i in range(1, n + 1):
            # 如果某个人的信任值等于 n - 1，说明他是法官
            if trust_map[i] == n - 1:
                return i
        # 如果没有找到符合条件的人，则返回 -1
        return -1


if __name__ == '__main__':
    print(Solution().findJudge(n=2, trust=[[1, 2]]))
    print(Solution().findJudge(n=3, trust=[[1, 3], [2, 3]]))
    print(Solution().findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]))
