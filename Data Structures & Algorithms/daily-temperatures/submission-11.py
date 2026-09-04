class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        penultimate = len(temperatures) - 2
        for l in range(penultimate, -1, -1):
            for r in range(l + 1, len(temperatures)):
                if results[r] == 0 and temperatures[r] <= temperatures[l]:
                    break
                elif temperatures[r] > temperatures[l]:
                    results[l] = r - l
                    break


        return results