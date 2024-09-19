# https://leetcode.cn/problems/length-of-the-longest-alphabetical-continuous-substring/?envType=daily-question&envId=2024-09-19
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans, cnt = 1, 1
        for i in range(len(s) - 1):
            cur, next = ord(s[i]), ord(s[i + 1])
            if next - cur == 1:
                cnt += 1
            else:
                cnt = 1
            ans = max(ans, cnt)
        return ans


if __name__ == '__main__':
    print(Solution().longestContinuousSubstring("abacaba"))
    print(Solution().longestContinuousSubstring("abcde"))
