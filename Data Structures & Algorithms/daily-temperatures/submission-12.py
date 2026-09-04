class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]
        end = len(temperatures) - 1
        for l in range(end - 1, -1, -1):
            for r in range(l + 1, end + 1):
                if results[end-r] == 0 and temperatures[r] <= temperatures[l]:
                    results.append(0)
                    break
                elif temperatures[r] > temperatures[l]:
                    results.append(r - l)
                    break

        results.reverse()
        return results