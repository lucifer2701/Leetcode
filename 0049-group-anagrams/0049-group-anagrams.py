class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        checkdic = {}
        for w in strs:
            dic[w] = "".join(sorted(w))
            if dic[w] not in checkdic:
                checkdic[dic[w]] = []
            checkdic[dic[w]].append(w)
        x=list(checkdic.values())
        x.sort(key=lambda y:len(y))
        return x