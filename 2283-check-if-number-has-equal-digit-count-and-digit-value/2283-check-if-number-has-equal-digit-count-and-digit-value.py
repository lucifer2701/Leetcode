class Solution:
    def digitCount(self, num: str) -> bool:
        mp=dict()
        for i in range(len(num)):
            if num[i] in mp.keys():
                mp[num[i]]+=1
            else:
                mp[num[i]]=1
        for i in range(len(num)):
            if str(i) in mp.keys():  pass
            else:
                mp[str(i)]=0
        for i in range(len(num)):
            if (int(num[i]))==mp[str(i)]: 
                pass
            else:   return 0
        return 1