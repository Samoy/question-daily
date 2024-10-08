from typing import List


# https://leetcode.cn/problems/find-products-of-elements-of-big-array/?envType=daily-question&envId=2024-08-23
class Solution:
    def findProductsOfElements(self, queries: List[List[int]]) -> List[int]:
        def sum_e(k: int) -> int:
            res = n = cnt1 = sum_i = 0
            for i in range((k + 1).bit_length() - 1, 0, -1):
                c = (cnt1 << i) + (i << (i - 1))  # 新增的幂次个数
                if c <= k:
                    k -= c
                    res += (sum_i << i) + ((i * (i - 1) // 2) << (i - 1))
                    sum_i += i  # 之前填的 1 的幂次之和
                    cnt1 += 1  # 之前填的 1 的个数
                    n |= 1 << i  # 填 1
            # 最低位单独计算
            if cnt1 <= k:
                k -= cnt1
                res += sum_i
                n |= 1  # 最低位填 1
            # 剩余的 k 个幂次，由 n 的低 k 个 1 补充
            for _ in range(k):
                lb = n & -n
                res += lb.bit_length() - 1
                n ^= lb  # 去掉最低位的 1（置为 0）
            return res

        return [pow(2, sum_e(r + 1) - sum_e(l), mod) for l, r, mod in queries]


if __name__ == '__main__':
    s = Solution()
    print(s.findProductsOfElements([[1, 3, 7]]))
    print(s.findProductsOfElements([[2, 5, 3], [7, 7, 4]]))
