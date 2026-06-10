class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        new_x = 0
        ori_x = x
        
        while x != 0:
            digit = x % 10
            x //= 10

            new_x = new_x * 10 + digit

        return ori_x == new_x 

# Improvemnt:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_x = 0
        
        while x > reversed_x: # It optimizes the previous O(N) aechitecture to O(N/2) by only reversing half of the number.
            digit = x % 10
            x //= 10

            reversed_x = reversed_x * 10 + digit

        return x == reversed_x or x == reversed_x // 10 # It prepares for both odd and even numbers. 