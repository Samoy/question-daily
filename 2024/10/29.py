from typing import List


# https://leetcode.cn/problems/generate-binary-strings-without-adjacent-zeros/?envType=daily-question&envId=2024-10-29
class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []

        def backtrack(path, remaining):
            # 当剩余长度为0时，说明已经构造了一个完整的字符串
            if remaining == 0:
                result.append(path)
                return

            # 如果当前路径长度大于等于1，检查最后一位是否是'0'
            if len(path) >= 1 and path[-1] == '0':
                # 如果是，那么下一个只能是'1'，避免出现两个连续的'0'
                backtrack(path + '1', remaining - 1)
            else:
                # 如果不是，那么下一个可以是'0'或'1'
                backtrack(path + '0', remaining - 1)
                backtrack(path + '1', remaining - 1)

        # 开始回溯过程，初始路径为空，剩余长度为n
        backtrack('', n)

        return result


if __name__ == '__main__':
    print(Solution().validStrings(3))
    print(Solution().validStrings(1))
