# leetcode_5th_longest_palindrome_substring

# Miscompilation 1:
from turtle import right


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) = 1 return s

        def isPalindrome(self, t_s: str) -> bool: # Indentation is the syntax for the block, but self is the reference for the method lookup.
                                                  # Although the line is indented, calling isOalindrome (without self) implies looking for a local variable or 
                                                  # a function defined inside the current longestPalindrome scope.

            t_m = {}
            t_left = 0
        
            while t_right in range(len(t_s)):
                if t_s[t_right] in t_m: # 0. Does this helper function really save memory? 
                    t_left = t_m[t_s[t_right]]
                
                    while t_left <= t_right:
                        if t_s[t_left + 1] == t_s[t_right - 1]:
                            t_left += 1
                            t_right -= 1
                        else: 
                            return False 
            
                t_m[t_s[t_right]] = t_right
                t_right += 1

            return True
        
        m = {}
        left = 0

        while right in range(len(s)):
            if s[right] in m:
                left = m[s[right]]

                if isPalindrome([left : right + 1]) == true: # The object shall be a string. What is missing to compile a full sliced string here?
                # The developer halts due to the redundancy.
                # What has been the complexity of this block so far
    
    # Solution:
    # 0. 
    # No. We only count how many times the function is called.  
    # The CPU must re-verify each character index in the O(n) scan for every possible O(n^2) substring pair.
    # So, O(n^3) cumulative cost exceeds memory-bus latency thresholds for N=1000.
    # CS always defines complexity by the upper bound (Big O) of the total execution path. Worst case: "aaaaaaaaa".
    # 1.
    # 
