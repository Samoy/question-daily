# https://leetcode.cn/problems/separate-black-and-white-balls/?envType=daily-question&envId=2024-06-06
class Solution:
    def minimumSteps(self, s: str) -> int:
        # 初始化答案变量ans为0，用于记录交换的总步数
        # 初始化sum变量为0，用于累计遇到的黑色球的数量
        cnt = sum = 0
        # 遍历输入的字符串s的每一个字符，下标范围为0到len(s)-1
        for i in range(len(s)):
            # 检查当前字符是否为'1'（代表黑色球）
            if s[i] == '1':
                # 若当前字符为'1'，则sum加1，表示遇到一个黑色球
                sum += 1
            else:
                # 若当前字符为'0'（代表白色球）
                # 则将当前累计的黑色球数量sum加到答案变量ans上
                # 这是因为，为了使白色球移动到左侧，所有在此白色球右侧的黑色球都需要至少一步交换到其右侧
                cnt += sum

        # 遍历结束后，返回最小交换步数ans
        return cnt


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumSteps("101"))
    print(solution.minimumSteps("100"))
    print(solution.minimumSteps("0111"))
    print(solution.minimumSteps("11000111"))
    print(solution.minimumSteps("111111111100100010"))
