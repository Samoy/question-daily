# https://leetcode.cn/problems/convert-date-to-binary/?envType=daily-question&envId=2025-01-01
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return "-".join([bin(int(i))[2:] for i in date.split("-")])


if __name__ == '__main__':
    print(Solution().convertDateToBinary("2080-02-29"))
    print(Solution().convertDateToBinary("1900-01-01"))
