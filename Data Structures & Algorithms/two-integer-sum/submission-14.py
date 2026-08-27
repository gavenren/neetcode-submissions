class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i,n in enumerate(nums):
            difference = target - n
            if difference in prev_map:
                return [prev_map[difference], i]
            prev_map[n] = i