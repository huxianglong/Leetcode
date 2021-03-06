class Solution:
    def totalNQueens(self, n: int) -> 'List[List[str]]':
        rows = [0] * n
        cols = [0] * n
        diags1 = [0] * (2 * n - 1)
        diags2 = [0] * (2 * n - 1)
        board = [['.'] * n for _ in range(n)]
        ans = 0
        def dfs(i):
            if i == n:
                # ans.append([''.join(ls) for ls in board])
                nonlocal ans
                ans += 1
                return
            for j in range(n):
                di1 = i + j
                di2 = n - 1 - i + j
                if (not cols[i] and not rows[j] and not diags1[di1] and not diags2[di2]):
                    cols[i], rows[j], diags1[di1], diags2[di2], board[i][j] = 1, 1, 1, 1, 'Q'
                    dfs(i + 1)
                    cols[i], rows[j], diags1[di1], diags2[di2], board[i][j] = 0, 0, 0, 0, '.'
        dfs(0)
        return ans

if __name__ == '__main__':
    sol = Solution()
    n = 4
    print(sol.totalNQueens(4))
