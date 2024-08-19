from collections import Counter


# https://leetcode.cn/problems/minimum-number-of-operations-to-make-word-k-periodic/description/?envType=daily-question&envId=2024-08-17
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        count = Counter(word[i: i + k] for i in range(0, n, k))
        return n // k - max(count.values())


if __name__ == '__main__':
    print(Solution().minimumOperationsToMakeKPeriodic("leetcodeleet", 4))
    print(Solution().minimumOperationsToMakeKPeriodic("leetcoleet", 2))
