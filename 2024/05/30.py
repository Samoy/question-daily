from collections import defaultdict


# https://leetcode.cn/problems/find-longest-special-substring-that-occurs-thrice-ii/description/?envType=daily-question&envId=2024-05-30
class Solution:
    def maximumLength(self, s: str) -> int:
        # 使用defaultdict来存储每个字符对应的连续出现长度列表
        groups = defaultdict(list)

        # 初始化计数器cnt，用于记录当前字符连续出现的次数
        cnt = 0

        # 遍历字符串s，利用enumerate获取索引i和字符ch
        for i, ch in enumerate(s):
            # 当前字符连续计数加1
            cnt += 1

            # 判断是否到达字符串末尾或下一个字符不同，如果是则处理当前字符的计数
            if i + 1 == len(s) or ch != s[i + 1]:
                # 将当前字符的连续计数添加到groups字典中对应字符的列表
                groups[ch].append(cnt)

                # 重置计数器
                cnt = 0

        # 初始化答案为0
        ans = 0
        # 遍历groups字典中的值（即各个字符的连续长度列表）
        for a in groups.values():
            # 对当前字符的连续长度列表进行降序排序
            a.sort(reverse=True)

            # 假设列表还可以扩展两个0，以简化后续的条件判断
            a.extend([0, 0])

            # 更新答案，考虑三种情况：
            # 1. 第一个最长连续子串减去2（确保至少出现三次）
            # 2. 第一个和第二个最长连续子串的较短者减去1（若两者都至少出现两次）
            # 3. 第三个最长连续子串（直接确保至少出现三次）
            ans = max(ans, a[0] - 2, min(a[0] - 1, a[1]), a[2])

        # 如果ans仍为0，说明没有找到满足条件的子字符串，返回-1
        return ans if ans else -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.maximumLength("aaaa"))
    print(solution.maximumLength("abcdef"))
    print(solution.maximumLength("abcaba"))
