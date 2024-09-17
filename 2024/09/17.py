from collections import defaultdict, deque
from typing import List

# https://leetcode.cn/problems/bus-routes/?envType=daily-question&envId=2024-09-17
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # ��¼������վ x �Ĺ��������
        stop_to_buses = defaultdict(list)
        for i, route in enumerate(routes):
            for x in route:
                stop_to_buses[x].append(i)

        # С�Ż������û�й��������������յ㣬ֱ�ӷ���
        if source not in stop_to_buses or target not in stop_to_buses:
            # ע��ԭ�� TP �����
            return -1 if source != target else 0

        # BFS
        dis = {source: 0}
        q = deque([source])
        while q:
            x = q.popleft()  # ��ǰ�ڳ�վ x
            dis_x = dis[x]
            for i in stop_to_buses[x]:  # �������о�����վ x �Ĺ����� i
                if routes[i]:
                    for y in routes[i]:  # ���������� i ��·��
                        if y not in dis:  # û�з��ʹ���վ y
                            dis[y] = dis_x + 1  # �� x վ�ϳ�Ȼ���� y վ�³�
                            q.append(y)
                    routes[i] = None  # ��� routes[i] ������

        return dis.get(target, -1)

if __name__ == '__main__':
    print(Solution().numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6))
    print(Solution().numBusesToDestination(routes = [[7,12],[4,5,15],[6]], source = 15, target = 12))
