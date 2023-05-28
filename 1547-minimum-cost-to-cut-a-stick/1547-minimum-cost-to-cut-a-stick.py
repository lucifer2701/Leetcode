class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        #Idea: Try and do all the cuts and see which one is the best
        # For each dp, we keep track of left and right
        @cache
        def dp(l, r):
            ans = float('inf')

            for cut in cuts:
                if l < cut < r:
                    ans = min(ans, r-l+dp(l,cut)+dp(cut,r))
            if ans == float('inf'):
                return 0
            return ans
        return dp(0,n)