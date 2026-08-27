class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums and difference in nums[i+1:]:
                if difference == nums[i]:
                    answer = [i, nums.index(difference, i+1)]
                    return answer
                answer = [i, nums.index(difference)]
                return answer

