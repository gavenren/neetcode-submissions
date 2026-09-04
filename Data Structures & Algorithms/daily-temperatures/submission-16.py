class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = [temperatures[0]]
        l = 0
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1]:
                while results[l] != 0:
                    l -= 1
                stack.pop()
                results[l] = i - l
                l -= 1
            stack.append(temperatures[i])
            l = i
        return results
        
