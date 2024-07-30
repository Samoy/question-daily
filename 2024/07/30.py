from typing import List


# https://leetcode.cn/problems/double-modular-exponentiation/?envType=daily-question&envId=2024-07-30
class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for i in range(len(variables)):
            v = variables[i]
            if pow(pow(v[0], v[1], 10), v[2], v[3]) == target:
                ans.append(i)
        return ans


if __name__ == '__main__':
    print(Solution().getGoodIndices(variables=[[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], target=2))
    print(Solution().getGoodIndices(variables=[[39, 3, 1000, 1000]], target=17))
