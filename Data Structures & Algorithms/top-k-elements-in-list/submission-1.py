from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)

        sorted_counts = dict(
            sorted(counts.items(), key=lambda item: item[1], reverse=True)
        )

        return list(sorted_counts.keys())[:k]