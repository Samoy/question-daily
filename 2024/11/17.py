from typing import List


# https://leetcode.cn/problems/friends-of-appropriate-ages/?envType=daily-question&envId=2024-11-17
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1

        ans = cnt_window = age_y = 0
        for age_x, c in enumerate(cnt):
            cnt_window += c
            if age_y * 2 <= age_x + 14:  # 不能发送好友请求
                cnt_window -= cnt[age_y]
                age_y += 1
            if cnt_window:  # 存在可以发送好友请求的用户
                ans += c * cnt_window - c
        return ans


if __name__ == '__main__':
    print(Solution().numFriendRequests([16, 16]))
    print(Solution().numFriendRequests([16, 17, 18]))
    print(Solution().numFriendRequests([20, 30, 100, 110, 120]))
