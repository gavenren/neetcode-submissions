class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        max_left = height[left_pointer]
        max_right = height[right_pointer]
        while left_pointer != right_pointer:
            if height[left_pointer] >= height[right_pointer]:
                right_pointer -= 1
                if height[right_pointer] >= max_right:
                    max_right = height[right_pointer]
                elif min(max_left, max_right) - height[right_pointer] > 0:
                    total_water += min(max_left, max_right) - height[right_pointer]
            else:
                left_pointer += 1 
                if height[left_pointer] >= max_left:
                    max_left = height[left_pointer]
                elif min(max_left, max_right) - height[left_pointer] > 0:
                        total_water += min(max_left, max_right) - height[left_pointer]


        return total_water