class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x<0:
            ans = int(str(x)[1:][::-1]) * -1
        else:
            ans = int(str(x)[::-1])
        
        if ans > 2**31 or ans < -2**31:
            return 0
        return ans
