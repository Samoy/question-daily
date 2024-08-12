from typing import List


# https://leetcode.cn/problems/implement-magic-dictionary/?envType=daily-question&envId=2024-08-12
class MagicDictionary:

    def __init__(self):
        self.words = list()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue

            diff = 0
            for chx, chy in zip(word, searchWord):
                if chx != chy:
                    diff += 1
                    if diff > 1:
                        break

            if diff == 1:
                return True

        return False


if __name__ == '__main__':
    md = MagicDictionary()
    md.buildDict(["hello", "leetcode"])
    print(md.search("hello"))
    print(md.search("hhllo"))
    print(md.search("hell"))
    print(md.search("leetcoded"))
