from itertools import pairwise


# https://leetcode.cn/problems/existence-of-a-substring-in-a-string-and-its-reverse/?envType=daily-question&envId=2024-12-26
class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        st = set()
        for x, y in pairwise(s):
            st.add((x, y))
            if (y, x) in st:
                return True
        return False


if __name__ == '__main__':
    print(Solution().isSubstringPresent("leetcode"))
    print(Solution().isSubstringPresent("abcba"))
    print(Solution().isSubstringPresent("abcd"))
