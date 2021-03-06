class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        map = {}
        for i in range(1, n + 1):
            if i == 1:
                map[i] = set(["()"])
                continue
            ans = set()
            for j in range(1, i // 2 + 1):
                for x in map[j]:
                    for y in map[i - j]:
                        ans.add(x + y)
                        ans.add(y + x)
                # [ans.add(x + y) and ans.add(y + x) for x in map[j] for y in map[i - j]]
            [ans.add("(" + x + ")") for x in map[i - 1]]
            map[i] = ans
        # def helper(n, map):
        #     ans = set()
        #     if n == 0:
        #         return ans
        #     if n == 1:
        #         ans.add("()")
        #         return ans
        #     for i in helper(n - 1):
        #         ans.add("(" + i + ")")
        #         ans.add(i + "()")
        #         ans.add("()" + i)
        #     return ans
        # return sorted(list(helper(n)))
        return list(map[n])

if __name__ == '__main__':
    n = 1
    n = 2
    n = 3
    n = 4
    # b = [[1, 3, 1], [2, 4, 2]]
    # b = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    sol = Solution()
    print(sol.generateParenthesis(n))

# ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
# ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","()((()))","()(()())","()(())()","()()(())","()()()()", "(())()()"]
# ['()(())()', '(())(())', '(()()())', '()()(())', '()(()())', '(()(()))', '((()()))', '()((()))', '(((())))', '(()())()', '()()()()', '((())())', '(())()()', '((()))()']