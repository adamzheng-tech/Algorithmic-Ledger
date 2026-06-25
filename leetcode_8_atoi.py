# leetcode_8

# Trial 1:
class Solution:
    def myAtoi(self, s: str) -> int:
        int = 0
        front_char = ["+", "-", " ", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        
        for i, char in enumerate(s):
            if s[0] in front_char:
                pass
            else:
                return 0
        
    # Although it is a good start, the developer needs to segment the whole procedure into the four required steps.

# Trial 2:
class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()

        sign = -1 if s[0] == "-" else 1

# Trial 3:
class Solution:
    def myAtoi(self, s: str) -> int:
        
        outcome = 0
        s = s.lstrip()

        if s and s[0] in ["-", "+"]:
            sign = -1 if s[0] == "-" else 1
            s = s[1:]
        else:
            sign = 1
        
        for i in range(len(s)):
            if s[i].isdigit() == True: #In Python, ".isdigit() == True" is considered redundant and goes against official style guidelines (PEP 8).
                outcome = outcome * 10 + int(s[i])
            else:
                return outcome * sign
        
        return outcome * sign

# Solution 1:
class Solution:
    def myAtoi(self, s: str) -> int:
        
        outcome = 0
        s = s.lstrip()

        if s and s[0] in ["-", "+"]:
            sign = -1 if s[0] == "-" else 1
            s = s[1:]
        else:
            sign = 1
        
        for i in range(len(s)):
            if s[i].isdigit():
                outcome = outcome * 10 + int(s[i])
            else:
                break
        outcome *= sign
        
        if outcome > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif outcome < -2 ** 31:
            return -2 ** 31
        else:
            return outcome
    
    # Is the code still viable if the developer runs it on a 32-bit disk?
    # 
    # No. Solution 2 is the key to this question.

# Solution 2:
class Solution:
    def myAtoi(self, s: str) -> int:
        
        outcome = 0
        s = s.lstrip()

        if s and s[0] in ["-", "+"]:
            sign = -1 if s[0] == "-" else 1
            s = s[1:]
        else:
            sign = 1
        
        for i in range(len(s)):
            if s[i].isdigit():
                if outcome > (2 ** 31 - 1 - int(s[i])) // 10:
                    return 2 ** 31 - 1 if sign == 1 else -2 ** 31
                outcome = outcome * 10 + int(s[i])
            else:
                break
        outcome *= sign

        return outcome