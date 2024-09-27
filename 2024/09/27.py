from collections import Counter


# https://leetcode.cn/problems/take-k-of-each-character-from-left-and-right/?envType=daily-question&envId=2024-09-27
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        if cnt['a'] < k or cnt['b'] < k or cnt['c'] < k:
            return -1
        mx = left = 0
        for right, ch in enumerate(s):
            cnt[ch] -= 1
            while cnt[ch] < k:
                cnt[s[left]] += 1
                left += 1
            mx = max(mx, right - left + 1)
        return len(s) - mx


if __name__ == '__main__':
    print(Solution().takeCharacters(s="aabaaaacaabc", k=2))
    print(Solution().takeCharacters(s="a", k=1))
