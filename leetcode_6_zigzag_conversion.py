# leetcode_6
# Miscompilation:
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        new_s = []
        for i, char in enumerate(s):
            period = 2 * (numRows - 1)
            row = min(i % period, period - i % period)

        # The developer doesn't know how to weave characters into different layers.
        # See the following solution to find out how.

# Correction:
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        new_s = [''] * numRows
        for i, char in enumerate(s):
            period = 2 * (numRows - 1)
            row = min(i % period, period - i % period)
            new_s[row] += char
        
        return ''.join(new_s)