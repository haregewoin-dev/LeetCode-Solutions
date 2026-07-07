class Solution:
    def reverse(self, x: int) -> int:
        neg = x< 0
        x = abs(x)
        reversedX= (str(x)[::-1])
        reversedX= int(reversedX)
        if reversedX>2**31 -1:
            return 0
        return -reversedX if neg else reversedX
            
