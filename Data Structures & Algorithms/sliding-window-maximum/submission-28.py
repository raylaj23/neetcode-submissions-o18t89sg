class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = [(-nums[i], i) for i in range(0, k)]
        heapq.heapify(pq)

        maxi, _ = pq[0]
        res = [-maxi]

        for i in range(k, len(nums)):
            heapq.heappush(pq, (-nums[i], i))
            maxi, poz = pq[0]
            
            while poz <= i-k and len(pq) >= k:
                maxi, poz = pq[0]
                if poz <= i - k:
                    maxi, poz = heapq.heappop(pq)

            res.append(-maxi)

        return res