from collections import defaultdict
from typing import List


# https://leetcode.cn/problems/accounts-merge/?envType=daily-question&envId=2024-07-15
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 并查集的查找函数，用于找到元素的根节点
        def find(p, i):
            if p[i] != i:
                # 路径压缩，直接将当前节点的父节点设为其根节点
                p[i] = find(p, p[i])
            return p[i]

        # 并查集的合并函数，用于合并两个集合
        def union(p, r, x, y):
            root_x = find(p, x)
            root_y = find(p, y)
            # 根据秩来决定哪个根节点作为新的根节点
            if root_x != root_y:
                if r[root_x] > r[root_y]:
                    p[root_y] = root_x
                elif r[root_x] < r[root_y]:
                    p[root_x] = root_y
                else:
                    p[root_y] = root_x
                    r[root_x] += 1

        # 创建字典，用于存储邮箱到账户名的映射
        email_to_name = {}
        # 创建字典，用于存储邮箱到ID的映射
        email_to_id = {}
        # 初始化ID计数器
        id_counter = 0
        # 初始化并查集的父节点列表
        parent = []
        # 初始化并查集的秩列表
        rank = []

        # 遍历每个账户
        for account in accounts:
            name = account[0]
            # 遍历账户中的每个邮箱
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = id_counter
                    # 将新ID添加到并查集的父节点和秩列表中
                    parent.append(id_counter)
                    rank.append(0)
                    id_counter += 1
                # 使用并查集合并账户中的所有邮箱，确保它们属于同一个集合
                union(parent, rank, email_to_id[account[1]], email_to_id[email])
                # 更新邮箱到账户名的映射
                email_to_name[email] = name
        # 创建字典，用于存储合并后的账户
        merged_accounts = defaultdict(list)
        # 遍历邮箱到ID的映射，将所有邮箱归类到它们所属的根节点下
        for email, idx in email_to_id.items():
            root_id = find(parent, idx)
            merged_accounts[root_id].append(email)
        # 创建结果列表，用于存储最终的合并账户
        result = []
        # 遍历合并后的账户，构建最终的输出格式
        for emails in merged_accounts.values():
            # 每个账户的第一个元素是账户名，其余元素是邮箱地址，按字符ASCII顺序排序
            result.append([email_to_name[emails[0]]] + sorted(emails))
        return result


if __name__ == '__main__':
    print(Solution().accountsMerge(
        [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
         ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))
    print(Solution().accountsMerge(
        [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"], ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
         ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"], ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
         ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]))
    print(Solution().accountsMerge([["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
                                    ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
                                    ["David", "David1@m.co", "David2@m.co"]]))
