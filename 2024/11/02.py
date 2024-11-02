# https://leetcode.cn/problems/number-of-bit-changes-to-make-two-integers-equal/?envType=daily-question&envId=2024-11-02
class Solution:
    def minChanges(self, n: int, k: int) -> int:
        return (n ^ k).bit_count() if (n & k) == k else -1


if __name__ == '__main__':
    print(Solution().minChanges(13, 4))
    print(Solution().minChanges(21, 21))
    print(Solution().minChanges(14, 13))
