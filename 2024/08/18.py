# https://leetcode.cn/problems/student-attendance-record-i/description/?envType=daily-question&envId=2024-08-18
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') < 2 and s.count('LLL') == 0


if __name__ == '__main__':
    print(Solution().checkRecord("PPALLP"))
    print(Solution().checkRecord("PPALLL"))
