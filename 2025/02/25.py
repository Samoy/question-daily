# https://leetcode.cn/problems/design-memory-allocator/?envType=daily-question&envId=2025-02-25
class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
        free = 0
        for i, id in enumerate(self.memory):
            if id > 0:  # 已分配
                free = 0  # 重新计数
                continue
            free += 1
            if free == size:  # 找到了
                self.memory[i - size + 1: i + 1] = [mID] * size
                return i - size + 1
        return -1  # 无法分配内存

    def freeMemory(self, mID: int) -> int:
        ans = 0
        for i, id in enumerate(self.memory):
            if id == mID:
                ans += 1
                self.memory[i] = 0  # 标记为空闲内存
        return ans


if __name__ == '__main__':
    allocator = Allocator(10)
    print(allocator.allocate(1, 1))
    print(allocator.allocate(1, 2))
    print(allocator.allocate(1, 3))
    print(allocator.freeMemory(2))
    print(allocator.allocate(3, 4))
    print(allocator.allocate(1, 1))
    print(allocator.allocate(1, 1))
    print(allocator.freeMemory(1))
    print(allocator.allocate(10, 2))
    print(allocator.freeMemory(7))
