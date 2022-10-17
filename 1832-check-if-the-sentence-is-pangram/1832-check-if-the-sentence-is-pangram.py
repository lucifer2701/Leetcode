class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        li=[sentence[i] for i in range(len(sentence))]
        li=set(li)
        if len(li)==26: return True
        return False