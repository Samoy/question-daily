# https://leetcode.cn/problems/lexicographically-smallest-string-after-operations-with-constraint/?envType=daily-question&envId=2024-07-27
class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        s = list(s)
        for i, c in enumerate(map(ord, s)):
            dis = min(c - ord('a'), ord('z') - c + 1)
            if dis > k:
                s[i] = chr(c - k)
                break
            s[i] = 'a'
            k -= dis
        return ''.join(s)


if __name__ == '__main__':
    print(Solution().getSmallestString("zbbz", 3))
    print(Solution().getSmallestString("xaxcd", 4))
    print(Solution().getSmallestString("lol", 0))
