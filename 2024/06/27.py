# https://leetcode.cn/problems/lexicographically-smallest-string-after-substring-operation/?envType=daily-question&envId=2024-06-27
class Solution:
    """
    给你一个仅由小写英文字母组成的字符串 s 。在一步操作中，你可以完成以下行为：
    选择 s 的任一非空子字符串，可能是整个字符串，接着将字符串中的每一个字符替换为英文字母表中的前一个字符。例如，'b' 用 'a' 替换，'a' 用 'z' 替换。
    返回执行上述操作 恰好一次 后可以获得的 字典序最小 的字符串。
    子字符串 是字符串中的一个连续字符序列。
    现有长度相同的两个字符串 x 和 字符串 y ，在满足 x[i] != y[i] 的第一个位置 i 上，如果  x[i] 在字母表中先于 y[i] 出现，则认为字符串 x 比字符串 y 字典序更小 。
    """

    def smallestString(self, s: str) -> str:
        arr, replace_index_list = list(s), []
        for i in range(len(arr)):
            if arr[i] == 'a':
                if len(replace_index_list) == 0:
                    continue
                else:
                    break
            else:
                replace_index_list.append(i)
        if not replace_index_list:
            arr[-1] = 'z'
        else:
            for index in replace_index_list:
                arr[index] = chr(ord(arr[index]) - 1)
        return ''.join(arr)


if __name__ == '__main__':
    print(Solution().smallestString("cbabc"))
    print(Solution().smallestString("acbbc"))
    print(Solution().smallestString("leetcode"))
    print(Solution().smallestString("aaa"))
