from collections import defaultdict
from typing import List

from sortedcontainers import SortedList


# https://leetcode.cn/problems/design-a-food-rating-system/?envType=daily-question&envId=2025-02-28
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_map = {}
        self.cuisine_map = defaultdict(SortedList)  # sortedcontainers
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_map[food] = [rating, cuisine]
            # 取负号，保证 rating 相同时，字典序更小的 food 排在前面
            self.cuisine_map[cuisine].add((-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.food_map[food]
        sl = self.cuisine_map[cuisine]
        sl.discard((-rating, food))  # 移除旧数据
        sl.add((-newRating, food))  # 添加新数据
        self.food_map[food][0] = newRating  # 更新 food 的 rating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_map[cuisine][0][1]


if __name__ == '__main__':
    foodRatings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                              ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                              [9, 12, 8, 15, 14, 7])
    print(foodRatings.highestRated("korean"))
    foodRatings.changeRating("sushi", 16)
    print(foodRatings.highestRated("japanese"))
    foodRatings.changeRating("ramen", 3)
    print(foodRatings.highestRated("japanese"))
    print(foodRatings.highestRated("korean"))
