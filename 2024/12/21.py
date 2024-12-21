from typing import List


# https://leetcode.cn/problems/sort-the-students-by-their-kth-score/?envType=daily-question&envId=2024-12-21
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda row: -row[k])
        return score


if __name__ == '__main__':
    print(Solution().sortTheStudents(score=[[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], k=2))
    print(Solution().sortTheStudents(score=[[3, 4], [5, 6]], k=0))
