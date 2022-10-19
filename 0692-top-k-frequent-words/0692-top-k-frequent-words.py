from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        temp=Counter(words)
        li=[]
        for ele in temp:
            li.append([ele,temp[ele]])
        li.sort(key=lambda x:x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(li[i][0])
        return ans