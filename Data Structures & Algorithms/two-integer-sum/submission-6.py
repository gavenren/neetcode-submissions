class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in hash_map:
                answer = [hash_map[nums[i]], i]
                return answer

            hash_map[difference] = i
