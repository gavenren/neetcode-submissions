class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1
        sorted_pairs = sorted(enumerate(position), key = lambda x: x[1])
        answer = len(position)
        current_max_time = (target - sorted_pairs[-1][1]) / speed[sorted_pairs[-1][0]]
        for i in range(len(position) - 2, -1, -1):
            time = (target - sorted_pairs[i][1]) / speed[sorted_pairs[i][0]]
            if time <= current_max_time:
                answer -= 1
            else:
                current_max_time = time
        return answer