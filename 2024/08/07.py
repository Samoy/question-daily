MOD = 1_000_000_007
MX = 1001

fac = [0] * MX  # f[i] = i!
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD


def comb(n: int, m: int) -> int:
    return fac[n] * inv_f[m] * inv_f[n - m] % MOD


# https://leetcode.cn/problems/find-all-possible-stable-binary-arrays-ii/?envType=daily-question&envId=2024-08-07
class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        if zero > one:
            zero, one = one, zero  # 保证空间复杂度为 O(min(zero, one))
        f0 = [0] * (zero + 3)
        for i in range((zero - 1) // limit + 1, zero + 1):
            f0[i] = comb(zero - 1, i - 1)
            for j in range(1, (zero - i) // limit + 1):
                f0[i] = (
                                f0[i]
                                + (-1 if j % 2 else 1)
                                * comb(i, j)
                                * comb(zero - j * limit - 1, i - 1)
                        ) % MOD

        ans = 0
        for i in range((one - 1) // limit + 1, min(one, zero + 1) + 1):
            f1 = comb(one - 1, i - 1)
            for j in range(1, (one - i) // limit + 1):
                f1 = (
                             f1
                             + (-1 if j % 2 else 1)
                             * comb(i, j)
                             * comb(one - j * limit - 1, i - 1)
                     ) % MOD
            ans = (ans + (f0[i - 1] + f0[i] * 2 + f0[i + 1]) * f1) % MOD
        return ans
