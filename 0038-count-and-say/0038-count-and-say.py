class Solution:
    def countAndSay(self, n: int) -> str:
	    dp = ["" for i in range(n+1)]
	    dp[1] = "1"
	    for i in range(2, n+1):
		    last_c = dp[i-1][0]
		    count = 0
		    for c in dp[i-1]:
			    if c == last_c:
				    count += 1
			    else:
				    dp[i] += str(count) + last_c
				    last_c = c
				    count = 1
		    dp[i] += str(count) + last_c
	    return dp[n]        