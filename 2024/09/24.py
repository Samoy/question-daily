# https://leetcode.cn/problems/maximize-number-of-subsequences-in-a-string/?envType=daily-question&envId=2024-09-24
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        """
        给你一个下标从 0 开始的字符串 text 和另一个下标从 0 开始且长度为 2 的字符串 pattern ，两者都只包含小写英文字母。
        你可以在 text 中任意位置插入 一个 字符，这个插入的字符必须是 pattern[0] 或者 pattern[1] 。注意，这个字符可以插入在 text 开头或者结尾的位置。
        请你返回插入一个字符后，text 中最多包含多少个等于 pattern 的 子序列 。
        :param text: 被插入的文本
        :param pattern: 所插入的文本
        :return: 最大子序列个数
        """
        x, y = pattern
        ans = cnt_x = cnt_y = 0
        for c in text:
            if c == y:
                ans += cnt_x
                cnt_y += 1
            if c == x:
                cnt_x += 1
        return ans + max(cnt_x, cnt_y)


if __name__ == '__main__':
    print(Solution().maximumSubsequenceCount("abdcdbc", "ac"))
    print(Solution().maximumSubsequenceCount("aabb", "ab"))
