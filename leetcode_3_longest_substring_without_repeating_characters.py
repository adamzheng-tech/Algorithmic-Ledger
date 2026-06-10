class Solution:

# Approach 1.
# Miscompilation 1:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        p = 0
        q = 1

        for p in range(len(s) - 1):
            if s[p] == s[q] and q < len(s):
                p += 1
                q += 1
            elif s[p] == s[q] and q == len(s):
                return 1
            elif s[p] != s[q] and q < len(s):
                q += 1
            else:
                return q - p # The problem is that the pointers only check the endpoints. The characters in between are bypassed.
        
        return q - p

# Miscompilation 2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        m = {}
        i = 0
        p = 0
        q = 1
        m[i] = s[p]

        for p in range(len(s) - 1):
            if q < len(s) - 1: # The condition truncates the upper evaluation bound (which is exactly len(s) - 1).
                if s[q] in m: # Python's in operator on a dictionary evaluates strictly against 
                              # memory addresses of the dictionary's keys, not its values. s[q] 
                              # is a string character, while m's keys are integers (i), resulti
                              # ng in a constant False evaluation.
                              # if s[q] in m.values(): (Note: This forces an O(n) scan, destroy
                              # ing dictionary efficiency. The true fix is changing the keys to
                              #  characters).
                    q += 1
                else:
                    i += 1
                    q += 1
                    m[i] = s[q]
            else:
                return len(m)
        return len(m)

# Miscompilation 3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        m = {}
        i = 0
        p = 0
        q = 1
        m[s[p]] = i

        for p in range(len(s) - 1):
            if q < len(s):
                if s[q] in m:
                    q += 1
                else:
                    i += 1
                    m[s[q]] = i
                    q += 1
            else:
                return len(m)
        return len(m) # This (compilation) block functions as a global Unique Character Counter. 
                      # It finds the "subsequence", which is explicitly avoided by the problem description.

# Miscompilation 4:
    def lengthOfLongestSubstring(self, s: str) -> int:

        m = {} 
        left = 0
        right = 1
        
        if not s:
            return 0
        
        max_length = 1
        i = 0
        m[s[left]] = i

        for left in range(len(s) - 1):
            if right < len(s):
                if not s[right] in m:
                    i += 1
                    m[s[right]] = i # Though it makes the index retrieval O(1), it is using a globally persistent Hash Map Memory, not a locally transient Sliding Window Memory.
                    max_length += 1
                    right += 1
                else:
                    left += 1 # The for loop (Python iterator) nullifies the manual window contraction. Left is overwritten in each iteration.
                    right += 1
                
        return max(max_length, right - left - 1)

# Miscompilation 5:
    def lengthOfLongestSubstring(self, s: str) -> int:

        m = {} 
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in m: # Edge case example: "abba". 
                m[s[right]] = right # Incorrect indentation.
                left = m[s[right]] + 1
            max_length = max(max_length, right - left + 1) 
        return max_length

# Miscompilation 6:
    def lengthOfLongestSubstring(self, s: str) -> int:

        m = {} 
        left = 0
        max_length = 0

        for right in range(len(s)):
            
            if s[right] in m:
                left = m[s[right]] + 1

            m[s[right]] = right
            max_length = max(max_length, right - left + 1) 
            
        return max_length

# Revision 1:
    def lengthOfLongestSubstring(self, s: str) -> int:

        m = {} 
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in m :
                left =max(left, m[s[right]] + 1)
            
            m[s[right]] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length

# Revision 2:
    def lengthOfLongestSubstring(self, s: str) -> int:

        m = {} 
        left = 0
        # right = 1 redundant
        max_length = 0

        for right in range(len(s)):
            if s[right] in m and m[s[right]] >= left: # Comapre it with the left =max(left, m[s[right]] + 1)". They have an equivalent functionality.
                left = m[s[right]] + 1

            m[s[right]] = right
            max_length = max(max_length, right - left + 1)
               
        return max_length




























    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
        
            char_set.add(s[right])

            max_length = max(max_length, right - left + 1)
        return max_length
