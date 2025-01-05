from sortedcontainers import SortedDict


# https://leetcode.cn/problems/my-calendar-iii/?envType=daily-question&envId=2025-01-04
class MyCalendarThree:
    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.d[start] = self.d.setdefault(start, 0) + 1
        self.d[end] = self.d.setdefault(end, 0) - 1

        ans = max_book = 0
        for freq in self.d.values():
            max_book += freq
            ans = max(ans, max_book)
        return ans


if __name__ == '__main__':
    my_calendar_three = MyCalendarThree()
    print(my_calendar_three.book(10, 20))
    print(my_calendar_three.book(50, 60))
    print(my_calendar_three.book(10, 40))
    print(my_calendar_three.book(5, 15))
    print(my_calendar_three.book(5, 10))
    print(my_calendar_three.book(25, 55))
