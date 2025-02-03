# https://leetcode.cn/problems/reverse-string-ii/?envType=daily-question&envId=2025-01-31
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        for i in range(0, len(s), k * 2):
            s[i: i + k] = s[i: i + k][::-1]  # 右端点自动和 n 取最小值
        return ''.join(s)


if __name__ == '__main__':
    print(Solution().reverseStr(s="abcdefg", k=2))
    print(Solution().reverseStr(s="abcd", k=2))
