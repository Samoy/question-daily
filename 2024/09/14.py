# https://leetcode.cn/problems/removing-stars-from-a-string/?envType=daily-question&envId=2024-09-14
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)


if __name__ == '__main__':
    print(Solution().removeStars("leet**cod*e"))
    print(Solution().removeStars("erase*****"))
