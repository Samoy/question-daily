# https://leetcode.cn/problems/my-calendar-ii/?envType=daily-question&envId=2025-01-03
class MyCalendarTwo:
    def __init__(self):
        self.tree = {}

    def update(self, start: int, end: int, val: int, l: int, r: int, idx: int) -> None:
        if r < start or end < l:
            return
        if start <= l and r <= end:
            p = self.tree.get(idx, [0, 0])
            p[0] += val
            p[1] += val
            self.tree[idx] = p
            return
        mid = (l + r) // 2
        self.update(start, end, val, l, mid, 2 * idx)
        self.update(start, end, val, mid + 1, r, 2 * idx + 1)
        p = self.tree.get(idx, [0, 0])
        p[0] = p[1] + max(
            self.tree.get(2 * idx, (0,))[0], self.tree.get(2 * idx + 1, (0,))[0]
        )
        self.tree[idx] = p

    def book(self, start: int, end: int) -> bool:
        self.update(start, end - 1, 1, 0, 10 ** 9, 1)
        if self.tree[1][0] > 2:
            self.update(start, end - 1, -1, 0, 10 ** 9, 1)
            return False
        return True


if __name__ == '__main__':
    cal = MyCalendarTwo()
    print(cal.book(10, 20))
    print(cal.book(50, 60))
    print(cal.book(10, 40))
    print(cal.book(5, 15))
