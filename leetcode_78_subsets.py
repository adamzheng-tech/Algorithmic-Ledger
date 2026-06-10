class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(start_index, current_path):
            result.append(current_path[:])
            for i in range(start_index, len(nums)):
                current_path.append(nums[i])
                backtrack(i + 1, current_path)
                current_path.pop()
        backtrack(0, [])
        return result