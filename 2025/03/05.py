# https://leetcode.cn/problems/break-a-palindromeÏ/?envType=daily-question&envId=2025-03-05Ï
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]
        return palindrome[:-1] + 'b'


if __name__ == '__main__':
    s = Solution()
    print(s.breakPalindrome("abccba"))
    print(s.breakPalindrome("a"))
