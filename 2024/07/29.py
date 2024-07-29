from typing import List


# https://leetcode.cn/problems/baseball-game/?envType=daily-question&envId=2024-07-29
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_list = []
        for o in operations:
            if o == '+':
                score_list.append(score_list[-2] + score_list[-1])
            elif o == 'C':
                score_list.pop()
            elif o == 'D':
                score_list.append(score_list[-1] * 2)
            else:
                score_list.append(int(o))
        return sum(score_list)


if __name__ == '__main__':
    print(Solution().calPoints(["5", "2", "C", "D", "+"]))
    print(Solution().calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))
