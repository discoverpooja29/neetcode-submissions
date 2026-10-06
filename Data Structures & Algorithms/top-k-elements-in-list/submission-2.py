from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        return [num for _, num in heapq.nlargest(k, ((f, n) for n, f in counts.items()))]    