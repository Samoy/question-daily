# https://leetcode.cn/problems/maximize-the-confusion-of-an-exam/?envType=daily-question&envId=2024-09-02
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        # 定义一个内部函数，用于计算最大连续相同字符的长度
        def maxConsecutiveChar(ch: str) -> int:
            """
            计算对于给定的字符ch，在改变最多k个字符的情况下，
            可以获得的最大连续ch字符的长度。

            :param ch: 一个字符，可以是'T'或'F'，表示需要连续的字符。
            :return: 一个整数，表示可以获得的最大连续ch字符的长度。
            """
            # 初始化最大长度、左指针位置和替换字符的计数
            ans, left, s = 0, 0, 0
            # 遍历答案键，右指针移动
            for right, c in enumerate(answerKey):
                # 如果当前字符不是ch，则计数加一
                s += c != ch
                # 当替换字符的计数超过k时，左指针右移，直到计数不超过k
                while s > k:
                    s -= answerKey[left] != ch
                    left += 1
                # 更新最大长度
                ans = max(ans, right - left + 1)
            return ans

        # 分别计算最大连续'T'和'F'的长度，返回其中较大的一个
        return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))


if __name__ == '__main__':
    print(Solution().maxConsecutiveAnswers("TTFF", 2))
    print(Solution().maxConsecutiveAnswers("TFFT", 1))
    print(Solution().maxConsecutiveAnswers("TTFTTFTT", 1))
