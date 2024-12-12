class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            m = max(gifts)
            i = gifts.index(m)
            gifts[i] = int(m**0.5)
        return sum(gifts)
        