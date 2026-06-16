# leetcode_4_median_of_two_sorted_arrays

# Miscompilation 1:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        med1 = (nums1[0] + nums1[-1]) / 2
        med2 = (nums2[0] + nums2[-1]) / 2

        if med1 < med2:
    # The developer halts here due to ambiguity of the usage of med1 and med2.
    # It works when m == n. 
    # Although the direction is not redundant, it is a notorious trap.

# Miscompilation 2:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        k = (m + n + 1) // 2
        i = (m + 1) // 2
        j = k - i

        while                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            if nums1[i - 1] <= nums2[j] and nums1[i] >= nums2[j - 1]:
                return min(nums1[i + 1], nums2[j + 1]) if (m + n)%2 == 0 else (nums1[i + 1] + nums2[j + 1]) / 2
            
            i = (i + 1)//2
    # Edge cases (e.g., nums1 = [1, 3], nums2 = [2]) should be included to the general rule.
    # Implementation of another if-else to handle the edge cases is redundant. 
    #
    # What is the root cause of the failure?
    # Binary search requires dynamic boundary pointers (left and right) to compress the search space, not a linear iterator.

# Correction:
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # 1. Hardware Constraint: Always search the smaller array to prevent 'j' bounds violation
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half_len = (m + n + 1) // 2
        
        while left <= right:
            i = (left + right) // 2
            j = half_len - i
            
            # 2. Virtual Boundary Padding (The Shield)
            # If the cut is at the absolute edge, assume the "empty" side is infinity
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            
            # 3. Partition Validation
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Correct partition found!
                if (m + n) % 2 == 1:
                    return float(max(nums1_left, nums2_left))
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
                    
            elif nums1_left > nums2_right:
                # nums1's left side is too big, squeeze the right boundary down
                right = i - 1
            else:
                # nums1's left side is too small, push the left boundary up
                left = i + 1

    # Q0: Why does the problem require a float output?
    # A : Consider the median of a dataset with an even number of elements.
    #     The sum of the two middle integers may not be an even number, which 
    #     dictates the necessity to return a float to ensure the mathematical accuracy.
    #
    # Q1: 