class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def str2int(num):
            val=0
            for i in num:
                val=val*10+(ord(i)-ord('0'))
            return val
        return str(str2int(num1)*str2int(num2))