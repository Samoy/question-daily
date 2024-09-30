from heapq import heappop, heappush, heapify


# https://leetcode.cn/problems/seat-reservation-manager/?envType=daily-question&envId=2024-09-3
class SeatManager:

    def __init__(self, n: int):
        # 构建小顶堆
        self.pq = list(range(1, n + 1))
        heapify(self.pq)

    # 弹出最小值
    def reserve(self) -> int:
        return heappop(self.pq)

    # 恢复
    def unreserve(self, seatNumber: int) -> None:
        heappush(self.pq, seatNumber)


if __name__ == '__main__':
    s = SeatManager(5)
    print(s.reserve())
    print(s.reserve())
    s.unreserve(2)
    print(s.reserve())
    print(s.reserve())
    print(s.reserve())
    print(s.reserve())
    s.unreserve(5)
