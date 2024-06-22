# https://leetcode.cn/problems/detect-capital/?envType=daily-question&envId=2024-06-23
class Solution:
    """
    我们定义，在以下情况时，单词的大写用法是正确的：
        1. 全部字母都是大写，比如 "USA" 。
        2.单词中所有字母都不是大写，比如 "leetcode" 。
        3. 如果单词不只含有一个字母，只有首字母大写， 比如 "Google" 。
    给你一个字符串 word 。如果大写用法正确，返回 true ；否则，返回 false 。
    """

    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


if __name__ == '__main__':
    print(Solution().detectCapitalUse("USA"))
    print(Solution().detectCapitalUse('FlaG'))
    print(Solution().detectCapitalUse('leetcode'))
    print(Solution().detectCapitalUse('Google'))
