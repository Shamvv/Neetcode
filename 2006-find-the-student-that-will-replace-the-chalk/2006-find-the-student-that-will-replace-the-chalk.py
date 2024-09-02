class Solution:
    def chalkReplacer(self, chalks: List[int], k: int) -> int:
        s = sum(chalks)
        n = k // s
        k -= s * n
        for kid, chalk in enumerate(chalks):
            if chalk > k:
                return kid
            k -= chalk