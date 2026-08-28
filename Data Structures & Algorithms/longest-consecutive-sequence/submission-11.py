class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        current = 1
        record = 1
        sorted_nums = sorted(set(nums))
        if len(sorted_nums) == 0:
            return 0
        if len(sorted_nums) == 1:
            return 1
        for i in range(1,len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1] + 1:
                current += 1
                if current > record:
                    record = current
            else:
                current = 1

        return record