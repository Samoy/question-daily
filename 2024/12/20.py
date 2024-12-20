from collections import Counter


# https://leetcode.cn/problems/minimum-length-of-anagram-concatenation/?envType=daily-question&envId=2024-12-20
class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for k in range(1, n // 2 + 1):
            if n % k:
                continue
            cnt0 = Counter(s[:k])
            for i in range(k * 2, n + 1, k):
                if Counter(s[i - k: i]) != cnt0:
                    break
            else:
                return k
        return n


if __name__ == '__main__':
    print(Solution().minAnagramLength("abba"))
    print(Solution().minAnagramLength("cdef"))
