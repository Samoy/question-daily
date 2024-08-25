# https://leetcode.cn/problems/permutation-difference-between-two-strings/description/?envType=daily-question&envId=2024-08-24
class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos = {c: i for i, c in enumerate(s)}
        return sum(abs(i - pos[c]) for i, c in enumerate(t))


if __name__ == '__main__':
    print(Solution().findPermutationDifference("abc", "bac"))
    print(Solution().findPermutationDifference("abcde", "edbac"))
