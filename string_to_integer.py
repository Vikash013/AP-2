class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        
        ans, sign = 0,1
        if s[0]=="-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        for char in s:
            if char.isdigit():
                ans = ans*10 + int(char)
            else:
                break
        ans *= sign
        
        minR = -(2**31)
        maxR = (2**31) - 1

        if ans >maxR:
            return maxR
        elif ans < minR:
            return minR
        else:
            return ans
