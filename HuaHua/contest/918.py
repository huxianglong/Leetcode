from __future__ import annotations


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        cur_max, cur_min, min_sum, max_sum, sum = 0, 0, A[0], A[0], 0
        for a in A:
            cur_max = max(cur_max + a, a)
            cur_min = min(cur_min + a, a)
            min_sum = min(min_sum, cur_min)
            max_sum = max(max_sum, cur_max)
            sum += a
        return max(max_sum, sum - min_sum) if max_sum > 0 else max_sum



if __name__ == '__main__':
    sol = Solution()
    s = [-2,-3,-1]
    s = [3,-2,2,-3]
    s = [5,-3,5]
    s = [3,-1,2,-1]
    s = [2,-2,2,7,8,0]
    s = [-2,4,-5,4,-5,9,4]
    s = [1, -2, 3, -2]
    print(sol.maxSubarraySumCircular(s))

