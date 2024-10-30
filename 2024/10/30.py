# https://leetcode.cn/problems/lexicographically-smallest-string-after-a-swap/?envType=daily-question&envId=2024-10-30
class Solution:
    def getSmallestString(self, s: str) -> str:
        t = list(s)
        for i in range(1, len(t)):
            x, y = t[i - 1], t[i]
            if x > y and ord(x) % 2 == ord(y) % 2:
                t[i - 1], t[i] = y, x
                break
        return ''.join(t)


if __name__ == '__main__':
    print(Solution().getSmallestString("45320"))
    print(Solution().getSmallestString("001"))
