class Solution:
    # 1278. 分割回文串 III
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        min_change = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                min_change[i][j] = min_change[i + 1][j - 1] + (1 if s[i] != s[j] else 0)

        f = min_change[0]
        for i in range(1, k):
            for r in range(n - k + i, i - 1, -1):
                f[r] = min(f[l - 1] + min_change[l][r] for l in range(i, r + 1))
        return f[-1]

    def checkPartitioning(self, s: str) -> bool:
        return self.palindromePartition(s, 3) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.checkPartitioning("abcbdd"))
    print(s.checkPartitioning("bcbddxy"))
