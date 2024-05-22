from typing import List


# https://leetcode.cn/problems/find-players-with-zero-or-one-losses/?envType=daily-question&envId=2024-05-22
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        我们以玩家为键，无论玩家胜利多少次（且没有输过，即值需要大于0）都标记为1。如果玩家失败了，则减去1。
        这样的话，如果玩家没有输过，则他的值就为1。输过1次，则值为0。输过多次，则值小于0。
        """
        d = dict()
        for match in matches:
            winner = match[0]
            loser = match[1]
            # 将胜利者标记为1
            if winner not in d:
                d[winner] = 1
            # 只有大于0，才说明该玩家没有输过
            elif d[winner] > 0:
                d[winner] = 1
            # 失败1次
            if loser not in d:
                d[loser] = 0
            # 失败多次
            else:
                d[loser] -= 1
        # 组装连胜者和只失败1次的玩家
        ans = [[], []]
        for key in d:
            value = d[key]
            if value > 0:
                ans[0].append(key)
            elif value == 0:
                ans[1].append(key)
        # 升序排列
        ans[0].sort()
        ans[1].sort()
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.findWinners([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
    print(s.findWinners([[2, 3], [1, 3], [5, 4], [6, 4]]))
