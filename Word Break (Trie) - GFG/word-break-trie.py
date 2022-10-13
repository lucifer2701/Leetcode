#User function Template for python3

class Trie:
    def __init__(self, words=[]):
        self.root = {}
        
        for word in words:
            self.add(word)
    
    def add(self, word):
        word += '$'
        curr = self.root
        
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
    
    def isPrefix(self, word):
        word += '$'
        curr = self.root
        
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]
        
        return True


class Solution:
    def solve(self, word, n, trie, i, memo):
        if i == n:
            return True
        if i in memo:
            return memo[i]
        
        for j in range(i+1, n+1):
            if trie.isPrefix(word[i:j]) and self.solve(word, n, trie, j, memo):
                memo[i] = True
                return True
        
        memo[i] = False
        return False
    
    def wordBreak(self, A, B):
        n = len(A)
        trie = Trie(B)
        memo = {}
        return self.solve(A, n, trie, 0, memo)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		ob=Solution()
		res = ob.wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends