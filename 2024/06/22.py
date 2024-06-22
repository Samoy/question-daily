# https://leetcode.cn/problems/lexicographically-smallest-beautiful-string/?envType=daily-question&envId=2024-06-22
class Solution:
    """
    如果一个字符串满足以下条件，则称其为 美丽字符串 ：
    它由英语小写字母表的前 k 个字母组成。
    它不包含任何长度为 2 或更长的回文子字符串。
    给你一个长度为 n 的美丽字符串 s 和一个正整数 k 。
    请你找出并返回一个长度为 n 的美丽字符串，该字符串还满足：
        在字典序大于 s 的所有美丽字符串中字典序最小。如果不存在这样的字符串，则返回一个空字符串。
        对于长度相同的两个字符串a和b，如果字符串a 在与字符串b不同的第一个位置上的字符字典序更大，则字符串a的字典序大于字符串b。
    例如，"abcd" 的字典序比 "abcc" 更大，因为在不同的第一个位置（第四个字符）上 d 的字典序大于 c 。
    """

    def smallestBeautifulString(self, s: str, k: int) -> str:
        a = ord('a')
        k += a
        s = list(map(ord, s))
        n = len(s)
        i = n - 1  # 从最后一个字母开始
        s[i] += 1  # 先加一
        while i < n:
            if s[i] == k:  # 需要进位
                if i == 0:  # 无法进位
                    return ""
                # 进位
                s[i] = a
                i -= 1
                s[i] += 1
            elif i and s[i] == s[i - 1] or i > 1 and s[i] == s[i - 2]:
                s[i] += 1  # 如果 s[i] 和左侧的字符形成回文串，就继续增加 s[i]
            else:
                i += 1  # 反过来检查后面是否有回文串
        return ''.join(map(chr, s))


if __name__ == '__main__':
    print(Solution().smallestBeautifulString("abcz", 26))
    print(Solution().smallestBeautifulString("dc", 4))
    print(Solution().smallestBeautifulString('dfa', 6))
    print(Solution().smallestBeautifulString('ced', 6))
