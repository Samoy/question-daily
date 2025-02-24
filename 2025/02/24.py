from typing import List


# https://leetcode.cn/problems/design-an-ordered-stream/?envType=daily-question&envId=2025-02-24
class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.stream = [None] * (n + 1)
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        if idKey == self.ptr:
            res = []
            while self.ptr <= self.n and self.stream[self.ptr]:
                res.append(self.stream[self.ptr])
                self.ptr += 1
            return res
        return []


if __name__ == '__main__':
    ordered_stream = OrderedStream(5)
    print(ordered_stream.insert(3, "ccccc"))
    print(ordered_stream.insert(1, "aaaaa"))
    print(ordered_stream.insert(2, "bbbbb"))
    print(ordered_stream.insert(5, "eeeee"))
    print(ordered_stream.insert(4, "ddddd"))
