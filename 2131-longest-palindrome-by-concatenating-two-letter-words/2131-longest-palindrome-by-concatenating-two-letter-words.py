class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        Map = Counter(words)
        ans = 0
        center = False
        
        for word, count in Map.items():
            if word[0]==word[1]:
                if count%2==0:
                    ans += count
                else:
                    ans += count-1
                    center = True
            elif word[0]<word[1]:
                ans += 2*min(count, Map[word[1]+word[0]])
        
        if center:
            ans+=1
        return 2*ans