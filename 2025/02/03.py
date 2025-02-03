# https://leetcode.cn/problems/valid-palindrome-ii/?envType=daily-question&envId=2025-02-03
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 初始化左右指针
        left, right = 0, len(s) - 1

        # 当左指针小于右指针时，进行循环
        while left < right:
            # 如果左右指针指向的字符不相等
            if s[left] != s[right]:
                # 检查跳过左指针或右指针后剩余部分是否为回文
                return s[left:right] == s[left:right][::-1] or s[left + 1:right + 1] == s[left + 1:right + 1][::-1]
            # 左指针右移，右指针左移
            left += 1
            right -= 1

        # 如果循环完成，说明字符串可以通过最多删除一个字符成为回文
        return True


if __name__ == '__main__':
    print(Solution().validPalindrome("aba"))
    print(Solution().validPalindrome("abca"))
    print(Solution().validPalindrome("abc"))
