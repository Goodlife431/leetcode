# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order
from collections import Counter
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        heap = []
        for num, count in counts.items():
            heapq.heappush(heap, (-count, num))

        top_k = [heapq.heappop(heap)[1] for _ in range(k)]

        return top_k