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
                # 1. What has been the complexity of this block so far?
    
    # Solution:
    # 0. 
    # No. We only count how many times the function is called.  
    # The CPU must re-verify each character index in the O(n) scan for every possible O(n^2) substring pair.
    # So, O(n^3) cumulative cost exceeds memory-bus latency thresholds for N=1000.
    # CS always defines complexity by the upper bound (Big O) of the total execution path. Worst case: "aaaaaaaaa".
    # 1.
    # O(n^2) time complexity, O(1) space complexity.

# Miscompilation 2:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s[0] and not s[1] except IndexError:
            return s
        
        current_len = 0
        max_len = 0

        for i in range(len(s)):
            if s[i] == s[i + 1]:
                while i - 1 >= 0 and i + 1 < len(s):
                    if s[i - 1] == s[i + 1]:
                        current_len = 
                    else: current_len = 2

    # The developer attempts to manually calculate index offsets (i - 1, i + 1) within a single loop structure.
    # It's "boundary condition hell/coupling".

# Miscompilation 3:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        current_s = []
        max_s = []

        def expand(left, right): # Remember, the helper function is indented inside LongestPalindrome, 
                                 # making it a closure (an "inside definition") and totally invisible to
                                 # the rest of the class (the global scope of the class).
            left = 0 
            right = 1 # The two pointers are overwritten in each call, nullifying the expansion logic.

            while left >= 0 and right < len(s) and s[left] == s[right]: # Good! Python evaluates and 
                                                                        # statements strictly from le
                                                                        # ft to right using short-circuit evaluation:
                                                                        # the right + 1 = len(s) 
                left -= 1
                right += 1
            
            return s[left + 1 : right] 
        
        for i in range(len(s)):
            current_s = expand(i, i+1)
            if len(current_s) > len(max_s):
                max_s = current_s

        return max_s

# Miscompilation 4:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        current_s = []
        max_s = []

        def expand(left, right):
            if s[left] == s[right] and right < len(s):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
            
                return s[left + 1 : right] 
            else:
                return []
            
            # Is this block minimalist?
            # ---
            # No. 0) Redundancy: it forces the CPU to evaluate s[left] == s[right] and right < len(s) twice.
            #     1) Sequence: it ignores the left-to-right feature of short-circuit evaluation.
            #        Even if "if..." is required, it should be written as "if right < len(s) and s[left] == s[right]" to avoid out-of-bounds access.
            #     2) Consistency: [] is not a string. (What is its type?)
            #     3) Efficiency: the s[left + 1 : right] (slice) can handle the empty string case natively. (How does it handle it? What is the result of s[0:0]? In Python, the expression s[0:0] returns an empty sequence of the same type as s (such as an empty string "", an empty list [], or an empty tuple ()).)

        for i in range(len(s)):
            current_s = expand(i, i + 1) if len(s) % 2 == 0 else current_s = expand(i, i) # Something is redundant here.
            
            if len(current_s) > len(max_s):
                max_s = current_s

        return max_s

# Miscompilation 5:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        current_s = []
        max_s = s[0]

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1 : right] 

        for i in range(len(s)):
            current_s = expand(i, i + 1) if len(s) % 2 == 0 else expand(i, i)
            # The len(s) actually can't dictate whether there is an odd-palindrome or an even palindrome.

            if len(current_s) > len(max_s):
                max_s = current_s

        return max_s

# Solution 1:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        max_s = s[0]

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left + 1 : right] 

        for i in range(len(s)):
            odd_s = expand(i, i)
            even_s = expand(i, i + 1)
            current_s = max(odd_s, even_s, key=len) # This line is a highly optimized, C-level evaluated
                                                    # assignment in Python. (Why does it override the lexicographical trap?)
            
            if len(current_s) > len(max_s):
                max_s = current_s

        return max_s

# Miscompilation 6:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s[0] and not s[1]:
            return s
        
        max_s = s[0]
        current_s = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            
            return s[left + 1: right]
        
        for i in range(len(s)):
            pal1 = expand(i, i)
            pal2 = expand(i, i + 1)
            current_s = max(pal1, pal2, key = len)

            max_s = current_s if current_s > max_s else max_s
        
        return max_s
    # Can you debug?
    # ---
    # 0. First constraint: -> "if len(s) < 2:".
    #    If len(s) <= 1: is not viable, because the developr has used max_s = s[0],
    #    An IndexError will emerge if the input is "".
    # 1. "current_s > max_s" compares ASCII/Unicode values, not the value the developer needs.