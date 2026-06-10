class Solution:
    
# Approach 1: Brute Force.
# Miscompilation:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        p = 0
        q = 1

        while p < len(nums) and q < len(nums): # Brittle pointer logic.
            complement = target - nums[p]

            if nums[q] == complement:
                return [p, q]
            else: 
                q += 1
        
            p += 1
            q = p + 1

# Revision:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        p = 0
        q = 1

        while p < len(nums) :
            complement = target - nums[p]

            if q < len(nums):
                if nums[q] == complement:
                    return [p, q]
                else: 
                    q += 1
            else:
                p += 1
                q = p + 1

        return []
        # The problem constraints explicitly confirms that there is one solution to each problem. In this case, is the return[] on the last line negligible?
        """### Architectural Analysis

The `return []` at the end of the function is **not** negligible; it is a critical safety constraint required by the compiler.

#### 1. Deterministic Return Paths

Even though the problem constraint guarantees exactly one solution, the **Python Interpreter** does not have access to that guarantee. It treats the function as a code block that *must* return a value regardless of the input. If the function concludes without hitting a `return` statement, Python implicitly returns `None`, which violates the type hint `-> List[int]`.

#### 2. Compiler Safety

In software engineering, this is known as a **"Dead Code"** path. While you, as the developer, know it is unreachable, the compiler treats it as a mandatory exit point. Omitting it will not trigger an error for the test cases that satisfy the constraint, but it renders the function fragile:

* **Logic Robustness:** If a test case were to violate the "exactly one solution" constraint (e.g., an empty array or a case with no target), your code would return `None` without the terminal return.
* **Runtime Integrity:** The `return []` acts as an assertion of failure. If the interpreter reaches the end, it signals that the algorithm failed to find a state match, which is safer than allowing an undefined return state.

### Architectural Truth

Strictly speaking, the `return []` is a **null-pointer safeguard**. In a production environment, you should never rely on problem constraints to dictate your control flow logic; you must always account for all possible execution paths (even theoretically impossible ones) to ensure the system remains stable under unexpected input conditions.
"""

# Approach 2: Hash Table (Two Passes).
# Miscompilation 1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        left = 0
        right = 0

        for left in range(len(nums) - 1):
            while right in range(len(nums) - 1): # The range(stop) function generates a sequence of integers that is exclusive of the stop value. It starts at 0 by default and stops right before it reaches the specified maximum.
                complement = target - nums[right]
                num_map[nums[right]] = right
                
                if complement in num_map and left < right:
                    return [num_map[complement], right]
                
                right += 1
        
        return []  

# Miscompilation 2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        left = 0
        right = 0

        for left in range(len(nums)):
            while right in range(len(nums)): 
                complement = target - nums[right]
                for i, nums[right] in enumerate(nums):
                    num_map[nums[right]] = i
                
                if complement in num_map and left < right:
                    return [num_map[complement], right]
                
                right += 1
        
        return []  

# Miscompilation 3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        left = 0
        right = 0
    
        for i, num in enumerate(nums):
            num_map[num] = i

        for left in range(len(nums)):
            
            while right in range(len(nums)): 
                complement = target - nums[right]
                
                if complement in num_map and left < right:
                    return [num_map[complement], right]
                
                right += 1
        
        return []  

# Revision 1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        left = 0
        right = 0

        for left in range(len(nums)):
            while right in range(len(nums)):
                complement = target - nums[right]
                num_map[nums[right]] = right
                
                if complement in num_map and left < right:
                    return [num_map[complement], right]
                
                right += 1
        
        return []  

# Revision 2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            num_map[num] = i
        
        for i in range(len(nums) - 1):
            complement = target - nums[i]
            if complement in num_map and num_map[complement] != i:
                return [num_map[complement], i]
            
        return []

# Approach 3: Hash Map (One Pass).
# Miscompilation:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map and num_map[complement] != i:
                return [num_map[complement], i]
            else: # Is it redundant?
                num_map[complement] = i # Is this line incorrect? Think.
                i += 1 # Python's for...in... loop—when combined with enumerate—manages the index i automatically based on the iterator's next state

        return []

# Revision:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map and num_map[complement] != i:
                return [num_map[complement], i]
            
            num_map[num] = i

        return []        