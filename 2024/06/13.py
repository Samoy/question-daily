from typing import List


# https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/?envType=daily-question&envId=2024-06-13
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        # 首先按照利润降序排列物品
        items.sort(key=lambda x: -x[0])

        # 初始化变量
        category_set = set()  # 用于存储已选中的不同类别
        res = 0  # 最大优雅度
        profit = 0  # 当前子序列的总利润
        st = []  # 辅助栈，存放未被计入不同类别的项目利润，用于替换时使用利润较低的项目

        # 遍历排序后的物品列表
        for i, item in enumerate(items):
            # 如果当前遍历的项目数未达到k
            if i < k:
                # 将利润累加到总利润
                profit += item[0]
                # 如果该类别已经在集合中（即不是新的类别）
                if item[1] in category_set:
                    # 将该项目的利润存入栈中，等待可能的替换
                    st.append(item[0])
                else:
                    # 否则，将类别添加到集合中
                    category_set.add(item[1])
            # 当前项目数等于k时，且遇到一个新的类别
            elif item[1] not in category_set and len(st) > 0:
                # 用当前项目的利润替换栈顶利润（即之前某个非新类别的利润）
                profit += item[0] - st.pop()
                # 将新类别添加到集合中
                category_set.add(item[1])

            # 在每一步计算当前的优雅度（总利润加上不同类别的平方）
            # 并更新最大优雅度
            res = max(res, profit + len(category_set) ** 2)

        # 返回最大优雅度
        return res


if __name__ == '__main__':
    print(Solution().findMaximumElegance([[3, 2], [5, 1], [10, 1]], 2))
    print(Solution().findMaximumElegance([[3, 1], [3, 1], [2, 2], [5, 3]], 3))
    print(Solution().findMaximumElegance([[1, 1], [2, 1], [3, 1]], 3))
