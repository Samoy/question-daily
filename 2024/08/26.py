from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


# https://leetcode.cn/problems/employee-importance/?envType=daily-question&envId=2024-08-26
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees = {e.id: e for e in employees}

        def dfs(id: int) -> int:
            e = employees[id]
            return e.importance + sum(dfs(sub) for sub in e.subordinates)

        return dfs(id)


if __name__ == '__main__':
    print(Solution().getImportance([Employee(1, 5, [2, 3]),
                                    Employee(2, 3, []), Employee(3, 3, [])], 1))
    print(Solution().getImportance([Employee(1, 2, [5]), Employee(5, -3, [])], 5))
