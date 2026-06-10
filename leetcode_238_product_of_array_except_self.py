class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix_accumulator = 1
        for i in range(n):
            answer[i] = prefix_accumulator
            prefix_accumulator *= nums[i]
        
        postfix_accumulator = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix_accumulator
            postfix_accumulator *= nums[i]
        
        return answer