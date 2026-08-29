class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall = 0
        right_wall = 0
        max_water = 0
        current_water = 0
        total_water = 0
        right_wall_index = 0
        for i in range(len(height)):
            if right_wall_index == len(height) - 1:
                break
            if height[i] > 0 and left_wall == 0:
                left_wall = height[i]
                right_wall_index = i
            if left_wall > 0 and i == right_wall_index:
                for h in range(i+1, len(height)):
                    if height[h] > right_wall:
                        right_wall = height[h]
                    if height[h] >= left_wall:
                        break
                for h in range(i+1, len(height)):
                    if height[h] == right_wall:
                        max_water += total_water
                        left_wall = right_wall
                        right_wall = 0
                        curren_water = 0
                        total_water = 0
                        right_wall_index = h
                        break
                    current_water = max(0, min(right_wall, left_wall) - height[h])
                    total_water += current_water
                    

        return max_water