from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ordered = Counter(nums)
        answer = []
        for number, counter in ordered.most_common(k):
            answer.append(number)
        return answer
