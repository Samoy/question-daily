# https://leetcode.cn/problems/clear-digits/?envType=daily-question&envId=2024-09-05
class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for c in s:
            if c.isdigit():
                st.pop()
            else:
                st.append(c)
        return ''.join(st)


if __name__ == '__main__':
    print(Solution().clearDigits("abc"))
    print(Solution().clearDigits("cb34"))
