class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        temp=dict()
        x=len(s)
        ans=[]
        if x<=10:   return ans
        for i in range(x-9):
            if s[i:i+10] in temp:
                temp[s[i:i+10]]+=1
            else:
                temp[s[i:i+10]]=1
        for ele in temp:
            if temp[ele]>1:
                ans.append(ele)
        return ans
                