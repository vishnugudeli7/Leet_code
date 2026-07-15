class Solution:
    def addDigits(self, num: int) -> int:
        
        while num>=10:
            s = 0
            while num>0:
                div = num%10
                s+=div
                num//=10
            num = s
        return num