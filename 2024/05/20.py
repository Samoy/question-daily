# https://leetcode.cn/problems/find-longest-awesome-substring/?envType=daily-question&envId=2024-05-20
class Solution:
    def longestAwesome(self, s: str) -> int:
        # 创建一个字典d，存储前缀子串的异或值到其结束索引的映射，初始值为-1
        d = {0: -1}
        # 初始化最长超赞子字符串长度为0，mask用于存储当前子串字符异或值
        ans, mask = 0, 0
        # 遍历字符串s的每个字符
        for i, c in enumerate(s):
            # 更新mask，将当前字符的二进制表示添加到mask中，ord(c) - ord('0')得到字符对应的数字
            mask ^= 1 << (ord(c) - ord('0'))
            # 如果mask在字典d中，说明之前遇到过相同的异或值，更新最长超赞子字符串长度
            if mask in d:
                ans = max(ans, i - d[mask])
            # 如果mask不在字典d中，将其添加并设置结束索引为i
            else:
                d[mask] = i
            # 遍历所有可能的字符异或值，检查是否能通过交换得到回文串
            for j in range(10):
                # 计算与当前mask异或的结果m
                m = mask ^ (1 << j)
                # 如果m在字典d中，表示有前缀子串与当前子串异或后形成回文串，更新最长超赞子字符串长度
                if m in d:
                    ans = max(ans, i - d[m])
        # 返回最长超赞子字符串的长度
        return ans