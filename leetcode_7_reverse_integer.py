class Solution:
# Compilation 1:
    def reverse(self, x: int) -> int:
        new_x = 0

        if x == 0:
            return 0

        l = len(str(abs(x))) # Converting to string forces O(n) space complexity and heap allocation for character arrays.
        
        if x > 0:
            for i in range(l):
                modulo = x % 10 
                x = x // 10
                new_x = new_x + modulo * (10 ** (l - i - 1))
            
            if new_x >= -2 ** 31 and new_x <= 2 ** 31 - 1: 
                return new_x
            else:
                return 0

        if x < 0:
            x = -x
            for i in range(l): # Violates DRY (Don't Repeat Yourself) principle, doubling the maintenance surface area.
                modulo = x % 10 
                x = x // 10
                new_x = new_x + modulo * (10 ** (l - i - 1)) # Exponentiation requires repeated multiplication, increasing CPU cycle counts per iteration.
            
            if new_x >= -2 ** 31 and new_x <= 2 ** 31 - 1: 
                return - new_x
            else:
                return 0
    # The coder needs to transit from procedural thinking (mapping the logic to human steps, like string conversion) to 
    # systems-level thinking (mapping logic to how the hardware actually processes data).

# Revision for Compilation 1:
    def reverse(self, x: int) -> int:
        
        sign = -1 if x < 0 else 1
        new_x = 0
        x = abs(x)
        
        INT_MAX = 2 ** 31 - 1 # Capitalized names stand for constants conventionally, but these are not actually constants in Python, as they can be reassigned.
        INT_MIN = -2 ** 31
        
        while x != 0:
            digit = x % 10 # Modulo is an operation. Digits combine to make numbers. (Compare: digit, numeral, and number.)
            x //= 10 # More efficient than x = x // 10, as it uses in-place floor division.
            
            if new_x > (INT_MAX - digit) // 10: # 0. What about new_x > (INT_MAX) // 10?
                return 0
            new_x = new_x * 10 + digit
        
        new_x = new_x * sign

        if new_x < INT_MIN or new_x > INT_MAX: # 1. Are there any edge cases?
            return 0
        
        return new_x

# To answer the 2 questions above, the revision for Compilation 1 is optimal for 
# unconstrained inputs. Since the problem statement specifies the input boundaries,
# the following solution is more efficient.
# (Solutions: Q0: No for unbounded input. Yes for this specified problem. 
#             Q1: Yes for unbouned input. No for this specified problem.)

    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        new_x = 0
        x = abs(x)

        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        while x != 0:
            digit = x % 10
            x //= 10

            if new_x > (INT_MAX - digit) // 10:
                return 0
            new_x = new_x * 10 + digit

        new_x = new_x * sign

        if new_x < INT_MIN or new_x > INT_MAX:
            return 0

        return new_x

# Even better solution:    

    def reverse(self, x: int) -> int:
        
        sign = -1 if x < 0 else 1
        new_x = 0
        x = abs(x)
        
        while x != 0 : # 0. What about x > 0? Functionally equivalent, architecturally different.  
            digit = x % 10
            x = x // 10
            if new_x > (2**31 - 1 - digit) // 10:
                return 0
            
            new_x = new_x * 10 + digit

        new_x = new_x * sign
        
        if new_x < -2**31 or new_x > 2**31 - 1:
            return 0
        
        return new_x
        
# Solution: Q0: 
#               Functionally equivalent: Because x can never be negative in this specific pipeline, 
#               x > 0 and x != 0 will terminate the loop on the exact same CPU cycle.
#               
#               Architecturally different: x != 0 is the industry standard for register exhaustion. 
#               The distinction lies in how the CPU's Arithmetic Logic Unit (ALU) evaluates conditions 
#               at the machine-code level. The assembly equivalent for x != 0 is JNZ and the assembly 
#               equivalent for x > 0 is JG. JNZ checks the zero flag (ZF), while JG checks both the si
#               gn (SF) and zero flags (ZF).

# Miscompilation 1:
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x <= 0 else 1
        x = sign * x

        reversed_x = 0

        while x != 0:
            digit = x % 10
            if x // 10 - digit <= 2^31 - 1:
                x = x // 10
                reversed_x = 10 * reversed_x + digit
        
        return sign * reversed_x
    
    # Test case: x = 900000, output = time limit exceeded.
    # Why?
    #
    # 0. 2 ^ 31 is an XOR calculation, not an exponentiation.
    # 1. "if x // 10 - digit <= 2^31 - 1:" isn't an effective overflow check.
    # 2. x //= 10 should execute unconditionally.    

# Correction for it:
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = sign * x

        reversed_x = 0

        while x != 0:
            digit = x % 10
            x //= 10

            if reversed_x > (2**31 - 1 - digit) // 10:
                return 0

            reversed_x = 10 * reversed_x + digit

        return sign * reversed_x