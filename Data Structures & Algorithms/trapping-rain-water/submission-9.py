class Solution:
    def trap(self, height: List[int]) -> int:
        total_water = 0
        end_index = len(height) - 1
        left_max = [height[0]]
        right_max = [height[-1]]
        for i in range(1, end_index):
            left_max.append(max(height[i], left_max[i-1]))
        for t in range(end_index - 1, 0, -1):
            right_max.append(max(height[t], right_max[end_index - 1 - t]))
        right_max.pop()
        left_max.pop()
        right_max.reverse()
        for h in range(1, end_index):
            shortest_wall = min(left_max[h-1], right_max[h-1])
            if shortest_wall > height[h]:
                total_water += shortest_wall - height[h]
        return total_water