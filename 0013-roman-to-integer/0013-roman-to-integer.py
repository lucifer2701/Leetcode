class Solution:
    def romanToInt(self, s: str) -> int:
        suma = 0
        s+="A"
        
        for i in range(len(s[:-1])):
            if s[i]=="M":
                suma+=1000
                
            elif s[i]=="D":
                suma+=500
                
            elif s[i]=="C" and (s[i+1]=="D" or s[i+1]=="M"):
                suma-=100
                
            elif s[i]=="C" and (s[i+1]!="D" or s[i+1]!="M"):
                suma+=100
                
            elif s[i]=="L":
                suma += 50
                
            elif s[i]=="X" and (s[i+1]=="L" or s[i+1]=="C"):
                suma -= 10
                
            elif s[i]=="X" and (s[i+1]!="L" or s[i+1]!="C"):
                suma += 10
            
            elif s[i]=="V":
                suma +=5
                
            elif s[i]=="I" and (s[i+1]=="V" or s[i+1]=="X"):
                suma -= 1
                
            elif s[i]=="I" and (s[i+1]!="V" or s[i+1]!="X"):
                suma += 1
            
        return suma